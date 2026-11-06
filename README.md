# NPS Night Sky Metrics Report Generator

Automates the first draft of an NPS Science Report Series night sky report from NSNSD ground-based camera data, satellite-modeled sky brightness (sALR), and census-based light-source data.

## Contents
1. [Project background](#project-background)
2. [What's in this repository](#whats-in-this-repository)
3. [Workflow at a glance](#workflow-at-a-glance)
4. [Step 1. Set up your workstation](#step-1-set-up-your-workstation)
5. [Step 2. Spatial analysis and mapping (ArcGIS Pro)](#step-2-spatial-analysis-and-mapping-arcgis-pro)
6. [Step 3. Data exploration](#step-3-data-exploration)
7. [Step 4. Report generation](#step-4-report-generation)
8. [Step 5. Finalize the report](#step-5-finalize-the-report)
9. [Reference](#reference)
10. [Troubleshooting](#troubleshooting)
11. [Public domain](#public-domain)

## Project Background
The Natural Sounds and Night Skies Division (NSNSD) collaborates with parks and partners to advance scientific understanding and inspire public appreciation of nighttime resources. NSNSD supports the study, preservation, and restoration of night skies and the nocturnal environment throughout the national park system by collecting data on night sky quality, conducting lighting inventories, assisting parks with star parties, and researching visitors' perceptions of lighting.

This project provides parks with published reports on night sky quality. Using data collected in parks, the final product is a report that parks can use for compliance, resource assessments, external reviews, and dark sky certification applications.

The intended audience is NSNSD staff who provide published reports to parks. The five-step process produces a fully formatted report following the NPS Science Report Series guidelines. The MS Word output is approximately 95% automated. The report author must update text that is bold and marked with a "~" character, and add other park-specific descriptions.

The NPS Science Report Series must:
1. Be peer-reviewed before submission.
2. Adhere to rigorous format requirements to ensure consistent presentation, compliance with NPS graphic identity standards, correct exporting, and application of Section 508 of the Rehabilitation Act.

The output is already formatted to the report template, so users do not need to adjust formatting manually.

**Additional tips**
1. Place the first draft in Teams: NSNSD > Planning > Night Sky Reports (create a park folder).
2. Use the [review log](https://doimspp.sharepoint.com/:x:/r/sites/nsnsdallstaff/_layouts/15/Doc.aspx?sourcedoc=%7B1E77E498-5CF3-4B6D-9823-1D0DA8BE9DA6%7D&file=NightSkiesNRR_review.xlsx&action=default&mobileredirect=true&wdLOR=cDE2BEA02-49FE-4950-8547-832828F1FF04) managed by Li-Wei when you are ready for internal review (internal).
3. Add template-specific comments to the [running log](https://doimspp.sharepoint.com/:x:/r/sites/nsnsdallstaff/_layouts/15/Doc.aspx?sourcedoc=%7B1D745879-5C41-48FD-A74B-2483F8994405%7D&file=Night%20Sky%20Report%20Template%20Updates.xlsx&action=default&mobileredirect=true&DefaultItemOpen=1&wdLOR=cFF6A13AC-5FBE-4D9A-B325-96BE56D0433C) (internal).
4. Advise park, internal, and admin reviewers to review in the Desktop MS Word app instead of the web app. The web app introduces errors that do not carry through to the desktop app.
5. Submit your manuscript to the [NR Pubs site](https://doimspp.sharepoint.com/sites/nps-NR-Pubs/SitePages/Home.aspx) after peer and park review (internal).

Examples: [Dinosaur National Monument report](https://irma.nps.gov/DataStore/DownloadFile/740932) | [NSNSD Night Sky Metrics Reports Data Collection Series](https://irma.nps.gov/DataStore/Collection/Profile/9562)

## What's in this repository

| File | Run in | Purpose |
|---|---|---|
| `ArcPro/NightSkyReportProcess/NightSkyScripts.ipynb` | ArcGIS Pro notebook | Creates the park folders, extracts the park boundary, calculates sALR zonal statistics, selects study sites, and builds the nearby-city (Walker's Law) table. |
| `LayoutScripts_ParkOverview.ipynb` | ArcGIS Pro notebook | Loads the park and study sites into the `ParkOverview` layout, applies symbology, zooms, renames layers, and turns on site labels. |
| `LayoutScripts_sALR.ipynb` | ArcGIS Pro notebook | Loads the park into the `sALR` layout, applies symbology, zooms to the park, and renames layers. |
| `NightSkyReporting/NSReportDataExplore.Rmd` | RStudio | Builds an HTML exploration report (tables, NPS-wide comparison, links) used to review a park's datasets. |
| `NightSkyReporting/NSreportmkdown.Rmd` | RStudio | Generates the formatted Word report (`NSreportmkdown.docx`). |
| `NightSkyReporting/template.docx` | (used by the Rmd) | Word reference template carrying the NPS Science Report styles. |

Folders the scripts read from and write to (under `NightSkyReporting`):

| Folder | Contents |
|---|---|
| `Figures/Common/` | Figures shared by all reports. The notebook copies them to each park's figure folder. |
| `Figures/<CODE>/` | Park-specific figures. You must add `park_geographic_location.png` and `sALR.png` (Step 2). |
| `Parks/<CODE>/` | Per-park inputs and outputs: `sALRoutput_<CODE>.xls`, `ReportParkNearTable_<CODE>.xlsx`, and `<CODE>_selection.csv` (saved dataset choices from Step 4). |
| `Reference/` | `NPMapsQuery.xlsx` (study site coordinates used by ArcGIS), `BortleClass.xlsx`, `NELM.xlsx`, `ModelSymbology.xlsx`. |

## Workflow at a glance

| Step | What you do | Tool | Main output |
|---|---|---|---|
| 1 | Install software, clone the repo, install the geodatabase | Git, RStudio, ArcGIS Pro | Working project |
| 2 | Run the spatial analysis and export two maps | ArcGIS Pro | `sALRoutput_<CODE>.xls`, `ReportParkNearTable_<CODE>.xlsx`, `park_geographic_location.png`, `sALR.png` |
| 3 | Review the park's datasets | `NSReportDataExplore.Rmd` | HTML exploration report |
| 4 | Choose datasets and generate the report | `NSreportmkdown.Rmd` | `NSreportmkdown.docx` |
| 5 | Edit the "~" text, rename, review, publish | MS Word | Final report |

## Step 1. Set up your workstation

### Step 1a. First-time setup (complete only once)
1. Install RStudio, R, ArcGIS Pro, and Git from Software Center.
2. Open a terminal (Git Bash) and navigate to the folder where you want the project:
   > `cd [path to the folder where you want to save the project]`
3. Clone the repository:
   > `git clone https://github.com/emeyer34/NightSkyMetricsReports.git`
4. Fetch and pull the latest changes:
   > `git fetch`
   > `git pull origin main`
5. In Windows Explorer, go to `NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting` and open `NightSkyReporting.Rproj`.
6. In the R project, open `NSreportmkdown.Rmd` and run the chunk labeled `packages` (play button at the top right of the chunk). This installs any missing packages and can take several minutes the first time. The script needs an internet connection: it downloads the NPS night sky dataset and the NPS units list each time it runs.
7. Download the geodatabase from the NSNSD Planning channel in Teams: [NightSkyReportProcess.gdb.zip](https://doimspp.sharepoint.com/:u:/r/sites/nsnsdallstaff/Shared%20Documents/Planning/Night%20Sky%20Reports/DataUpdates/NightSkyReportProcess.gdb.zip?csf=1&web=1&e=oxb9yM). It holds the latest sALR model and census data, and users are notified when a new version is available. Extract its contents into `NightSkyMetricsReports\NightSkyReportGenerator\ArcPro\NightSkyReportProcess`.

### Step 1b. Pull updates (before each new report)
1. Open a terminal in the project folder.
2. Pull the latest changes:
   > `git pull`
3. If `git pull` fails because of local modifications, you can overwrite your local changes with:
   > `git fetch --all`
   > `git reset --hard origin/main`

   (Confirm the default branch name for your clone; earlier versions of this guide said `master`.)
4. Check the Teams folder for a newer geodatabase and re-extract it if one is posted.

## Step 2. Spatial analysis and mapping (ArcGIS Pro)
1. Open `NightSkyReportProcess.aprx` and select the `Processing Map`.
2. Open `NightSkyScripts.ipynb`. In the user-input cell, set:
   - `unitcode` and `park` to the four-letter park code (for example `BISC`).
   - `buffnum`: buffer distance in km for parks with monitoring sites on or near the boundary (default 10).
   - `citydist`: search distance in km from sites to cities (default 300).
   - `repgen`: the path to your local `NightSkyReportGenerator` folder. This is the only path you need to edit.

   Then choose `Run All` in the `Cells` menu. The notebook creates `Figures\<CODE>` and `Parks\<CODE>`, copies the common figures, and exports `sALRoutput_<CODE>.xls` and `ReportParkNearTable_<CODE>.xlsx` to `Parks\<CODE>`.
3. **Park overview map**
   1. Open the `ParkOverview` layout and select the `StudySites` map. Remove any existing park or study-site layers.
   2. Run all cells in `LayoutScripts_ParkOverview.ipynb`.
   3. Return to the layout and refine labels and zoom. Double-click the map title so the dynamic text shows the `Unit_Name` from the park boundary file.
   4. Export the layout to `NightSkyReporting\Figures\<CODE>` and replace the existing `park_geographic_location.PNG`.
4. **sALR map**
   1. Select the `ALR_PARK` map in the sALR layout. Remove any existing park boundary layers.
   2. Run all cells in `LayoutScripts_sALR.ipynb`.
   3. Adjust the map to include nearby areas that may influence ALR results, and update the title text to the `Unit_Name`.
   4. Export the layout to `NightSkyReporting\Figures\<CODE>` and replace the existing `sALR.PNG`.

## Step 3. Data exploration
1. Open `NightSkyReporting.Rproj`, then open `NSReportDataExplore.Rmd`.
2. In the Knit dropdown, choose `Knit with Parameters`, enter the four-letter park code, and click `Knit`.
3. The HTML report is saved next to the `.Rproj` file. Use it to review every dataset for the park: site names, dates, dataset IDs (`DNIGHT`), metrics tables (Tables 1 and 2), the comparison to the entire NPS dataset, and the links to each dataset's NPMaps report and images.
4. Decide, and write down, three things for Step 4:
   - **Site of interest**: the single dataset whose images appear on the cover and in Figures 3 and 4. It can be a high-value dark site or one affected by skyglow.
   - **Summary datasets**: the datasets whose data are averaged or listed in the text and in Tables 1, 2, 4 and 5.
   - **Appendix A datasets**: the datasets whose notes and image links are listed in Appendix A.
   - Also note any datasets that share a site name but should be reported as separate sites.

Keep the exploration report open for Step 4.

## Step 4. Report generation
1. In the same R project, open `NSreportmkdown.Rmd` and choose `Knit with Parameters`.
2. Fill in the parameter form:

   | Parameter | What to enter |
   |---|---|
   | `alpha_code` | Four-letter park code, for example `BISC`. The full park name is looked up automatically from the NPS units list, so there is no park-name field. |
   | `viirsyear` | Year of the VIIRS composite used in the sALR model (default 2024). |
   | `censusyear` | Census year used for city populations (default 2020). |
   | `sdist` | Source distance in km (default 300, maximum 300). |
   | `selection_file` | Leave blank to open the selection windows. To repeat an earlier run, enter the path to its saved `Parks\<CODE>\<CODE>_selection.csv`. |

   Accept the default ALR and census values unless the project manager says otherwise.
3. Click `Knit`. A selection window opens (it may appear behind RStudio; check the taskbar).
   - **Window 1: dataset selection.** Every dataset for the park is listed as `DNIGHT | Site | Date` in three panels. Pick exactly one site of interest (left panel). Select the summary datasets (middle panel) and the Appendix A datasets (right panel). Use Ctrl+click or Shift+click to select several, or `Select all`. Click `Run report`. The report will not run until the site of interest, at least one summary dataset, and at least one Appendix A dataset are chosen.
   - **Window 2: duplicate site names (appears only when needed).** If selected datasets share a site name, they are listed with date, coordinates, and elevation. Edit a name to report that dataset as a separate site, or leave it unchanged to keep it as the same site. Click `Continue`.
4. After about 5 to 20 seconds, a Word document is generated and saved as `NSreportmkdown.docx` next to the `.Rproj` file. The console shows a line starting `Selection - SOI:` listing the dataset IDs used, which you can check before opening the report.

### How the selections are used

| Selection | Where it appears in the report |
|---|---|
| Site of interest | Cover image, Figures 3 and 4 and their captions, and Table 3 (nearby cities). |
| Summary datasets | Number of sites and observations, date range, averages in the abstract and Results, and Tables 1, 2, 4 and 5. |
| Appendix A datasets | Appendix A observation notes and image links. |

The site of interest does not have to be in the other two sets, but the script warns if it is not.

### Saved selection and re-knitting
Each run saves `Parks\<CODE>\<CODE>_selection.csv`. It records the original site name, the name used in the report (`SITE_NAME_REPORT`), and 1/0 flags for `soi`, `summary` and `appendix`. Enter its path in `selection_file` to re-knit with the same choices and skip both windows. You can edit the CSV to change selections or renames. A CSV saved before site renaming existed has no `SITE_NAME_REPORT` column, so re-run once to create the new format.

### Automatic wording for small datasets
The text adjusts to how much data you include:

| Situation | Behavior |
|---|---|
| One date | The date is reported once ("on June 5, 2012") instead of a range ("from X to Y"). |
| One site | Singular wording ("1 site", "The data collection site is listed in Table 2"). |
| One summary dataset | Averages are described as measured values: "measured" instead of "average" for zenith brightness, horizontal illuminance and NELM; "observed" instead of "most common" for Bortle Class; and a single ALR value instead of a min-max range. |
| Several datasets | Ranges, averages, and plural wording are used as before. |

Averages of the natural sky (for example, "average natural levels") and the modeled whole-park ALR are not affected. If you keep several dates for one site, the report still describes averages across those dates.

### Duplicate site names
Renaming happens only in the report. The nearby-city table (Table 3) is matched on the original NPS site name, so the city list for a renamed site of interest still works.

## Step 5. Finalize the report
1. Move the HTML report from Step 3 and the Word report from Step 4 to `NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting\Parks\<CODE>`.
2. Rename both documents so they identify the park.
3. In the Word document, update all text that is bold and marked with "~".
4. Once the documents are finalized and reviewed, they are ready for publication.

## Reference

### Required inputs by step
| Needed by | Input | Source |
|---|---|---|
| Step 2 | `NightSkyReportProcess.gdb` (sALR raster, census cities, park boundaries) | NSNSD Teams, Planning channel |
| Step 2 | `Reference\NPMapsQuery.xlsx` (study site coordinates) | Maintained by the project manager from the NPS night sky GeoJSON; confirm it is current for your park |
| Step 4 | `Parks\<CODE>\sALRoutput_<CODE>.xls`, `ReportParkNearTable_<CODE>.xlsx` | Step 2 |
| Step 4 | `Figures\<CODE>\` figures | Step 2 and `Figures\Common` |
| Step 4 | `Reference\BortleClass.xlsx`, `NELM.xlsx`, `ModelSymbology.xlsx`, `template.docx` | Repository |
| Steps 3 and 4 | Live data: the NPS night sky GeoJSON and the NPS units list | Internet connection required |

### Software requirements
R, RStudio, ArcGIS Pro (with the 3D, Spatial, Image and Image Analyst extensions), and Git. The selection windows use the `tcltk` package, which ships with R on Windows. Mac users need XQuartz.

## Troubleshooting

| Problem | What to try |
|---|---|
| Selection window does not appear | Look for it behind RStudio in the taskbar. On a Mac, install XQuartz. As a workaround, supply a `selection_file`. |
| "Park code ... was not found in the NPS units list" | Check the code for typos, and confirm the connection to irmaservices.nps.gov. |
| "Required file ... not found" | Confirm the `Parks\<CODE>` and `Figures\<CODE>` folders were created by Step 2 and that the file names use the same park code. |
| Table 3 or city lists are empty | The site of interest and its dataset ID must match the near-table from Step 2. Check that `NPMapsQuery.xlsx` was current when Step 2 ran. |
| Fewer datasets than expected in the report | Check the `Selection - SOI:` message and the saved selection CSV. |
| Numbers with thousands separators print with a space (for example "1 120") | The script wraps `percent()` to use a comma. Keep that wrapper after the library calls in the `packages` chunk. |
| Figures 3 and 4 are missing | The site of interest has no image link in the NPS data. The report shows "not available" and continues. |
| Warnings about missing Bortle, NELM, SQM or ALR values | These metrics were not collected for the selected datasets. The report prints placeholders for you to edit. |

### Public domain

This project is in the worldwide [public domain](LICENSE.md):

> This project is in the public domain within the United States,
> and copyright and related rights in the work worldwide are waived through the
> [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication.
> By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
