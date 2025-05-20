
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import openpyxl
from datetime import datetime

# Parameters setup
params = {
    "fullname": "National Park",
    "alpha_code": "LAVO",
    "viirsyear": 2023,
    "censusyear": 2020,
    "sdist": 300,
    "soi": "Lassen Peak",
    "soidset": "LAVO070716",
    "soidate": "Month DD, YYYY"
}


# Load required packages (install if not available)
# In Python, you typically manage dependencies through requirements.txt or conda environments.

# Function to load GeoJSON data
def load_geojson(url):
    response = requests.get(url)
    return response.json()

# Load dataset
data = load_geojson("https://www.nps.gov/subjects/nightskies/nsdmap.geojson")

# Convert to DataFrame
df = pd.json_normalize(data['features'])

# Extract and convert coordinates
df['LATITUDE'] = df['geometry'].apply(lambda x: x['coordinates'][1])
df['LONGITUDE'] = df['geometry'].apply(lambda x: x['coordinates'][0])
df['parkcode'] = df['properties.DNIGHT'].str[:4]

# Filter the dataset based on the park code
repdata = df[df['parkcode'] == params['alpha_code']].copy()
repdata['Date'] = pd.to_datetime(repdata['properties.MID_DATE_LMT'], format="%m/%d/%Y")

# Data wrangling
sitenum = repdata['properties.SITE_NAME'].nunique()
daynum = repdata['properties.DNIGHT'].nunique()
edate = repdata['Date'].min()
ldate = repdata['Date'].max()

avebright = round(repdata['properties.ZENITH_LUM_MSA'].mean(), 2) if not repdata['properties.ZENITH_LUM_MSA'].isnull().all() else 'not measured'
avestarvis = round(repdata['properties.VISSTARS_PCT'].mean(), 2) if not repdata['properties.VISSTARS_PCT'].isnull().all() else 'not measured'

# Average and extreme ALR values
aveALR = round(repdata['properties.ALR_POS'].mean(), 2) if not repdata['properties.ALR_POS'].isnull().all() else 'not measured'
minALR = round(repdata['properties.ALR_POS'].min(), 2) if not repdata['properties.ALR_POS'].isnull().all() else 'not measured'
maxALR = round(repdata['properties.ALR_POS'].max(), 2) if not repdata['properties.ALR_POS'].isnull().all() else 'not measured'

# Determine ALR category
if pd.isna(aveALR):
    alrcat = "not readily visible"
elif aveALR <= 0.3:
    alrcat = "excellent"
elif aveALR <= 2.0:
    alrcat = "impaired"
else:
    alrcat = "not readily visible"

# Bortle Class analysis (using dummy data)
bortle_class = pd.read_excel(".//Reference//BortleClass.xlsx")  # Ensure you have this file
bortle_mode = repdata['properties.BORTLE'].mode()[0]
bortletable = bortle_class[bortle_class['class'] == bortle_mode]

bortcat = bortletable['category'].values[0]
bortdesc = bortletable['description'].values[0]

# NELM description analysis
avenelm = repdata['properties.ZLM'].mean() if not repdata['properties.ZLM'].isnull().all() else 'not measured'

nelm_description = pd.read_excel(".//Reference//NELM.xlsx")  # Ensure you have this file
nelmcat = nelm_description.loc[(nelm_description['nelm'] - avenelm).abs().idxmin()]['description']

# ALR Model Output
alrmodel = pd.read_excel(f".//Parks//{params['alpha_code']}//sALRoutput_{params['alpha_code']}.xls")

# Generate report summary
report_summary = f"""
# Abstract
This report characterizes night sky conditions in {params['fullname']} ({params['alpha_code']}) using measurements made in the park unit and models of regional conditions based on satellite data. Calibrated night sky imagery was obtained to characterize the night sky at {sitenum} sites. These ground-based observations were collected on {daynum} nights from {edate.date()} to {ldate.date()}. 

The zenith brightness is {avebright} mag/arcsec^2^. We estimate more than {avestarvis}% naked eye stars were visible throughout the data collection period. The whole sky over {params['alpha_code']} is between {minALR} - {maxALR} (mean={aveALR}) brighter than average natural levels, indicating {alrcat} dark sky conditions on average.

In {params['alpha_code']}, we classified the sky as Bortle Class {bortle_mode}: {bortcat}, based on the visibility of astronomical objects. The naked eye limiting magnitude (NELM) is {avenelm}, which is approaching {nelmcat}. 
"""

print(report_summary)