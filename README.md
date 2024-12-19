# NPS Night Sky Metrics Report Generator
## Example
This README is under construction

This is a four step process to create night sky metrics reports that are formatted into the NPS science report series word template. Examples of the final product can be found by NPS employees here. https://irma.nps.gov/DataStore/Collection/Profile/9562
## Order of Operations

### 1. Spatial analysis and mapping
   a.)Make sure you have the latest gdb. This will have the most recent ALR model. NPS employees can find it in the NSNSD Sharepoint Software and Scripts folder, named NightSkyReportProcess.gdb.zip. Extract contents into the project folder: NightSkyMetricsReports\NightSkyReportGenerator\ArcPro\NightSkyReportProcess
  
  b.) Open NightSkyReportProcess.aprx
  
  c.) Select the Processing Map
  
  d.) In NightSkyScripts.ipynb, change the file path stored as "repgen" to your local project folder. Change the park unit code to the park you are reporting on. In Cells, select Run All
  
  e.) Select the StudySites map in the ParkOverview Layout. Remove any old park study sites or boundary layers.
  
  f.) In LayoutScripts_ParkOverview, Cells, select Run All
  
  g.) Return to the ParkOverview Layout and fine tune the map by modifying labels, zoom, if needed. Double click on the Map title and update the dynamic text from the Park Unit boundary file to display the Unit_Name. When satisfied, export the layout by navigating to the park unit code that was created in the following location: NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting\Figures. In the folder of the park unit you are working on, replace the file named: park_geographic_location.PNG
  
  h.) Select the ALR_PARK map in the sALR layout. 
  
  i.) In LayoutScripts_sALR, Cells, select Run All
  
  j.) Return to the sALR layout and fine tune the map to include nearby areas that could be influencing the ALR results. Double click on the Map title and update the dynamic text from the Park Unit boundary file to display the Unit_Name. When satisfied, export the layout by navigating to the park unit code that was created in the following location: NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting\Figures. In the folder of the park unit you are working on, replace the file named: sALR.PNG

### 2. Data Exploration
  a.) Navigate to the following location: NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting. Open NightSkyReporting.Rproj
  
  b.) In the project, open RMarkdown document, NSReportDataExplore.Rmd; In the Knit dropdown button, choose "Knit with Parameters"
  
  c.) A data form will appear and type in the park unit code and select Knit
  
  d.) This will create an HTML report that will be saved in the same location as the .Rproj file. Use this report to explore the focal park unit night sky data. Choose from this snapshot report the study site that you will highlight as the site of interest for the larger published report. It is advised to keep this report open for Step 3.

### 3. Report Generation
  a.) In the same R project as step 2b, open the NSreportmkdown.Rmd.
  
  b.) Once open, in the Knit dropdown button, choose "Knit with Parameters"
  
  c.) A data form will appear. Enter the park name and unit code. Accept defaults for the ALR model and census data used (unless otherwise told by project manager). Use the html report from Step 2 to fill out the appropriate information for the Site of Interest. 
  
  d.) Select Knit. After ~5-20 seconds, a word document will appear with a fully formated report. This document will also be saved as NSreportmkdown.docx in the same location as the .Rproj

### 4. Finalize Report
  a.) Move both reports from steps 2 & 3 to the park folder in the following location: NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting\Parks
  
  b.) It is advised to rename to associate each document with the park.
  
  c.) In the word document, update all text that is bold and noted by "~".
  
  c.) Once finalized and reviewed, it is ready for publication. 

  

## License

## Publications

 https://irma.nps.gov/DataStore/Collection/Profile/9562

