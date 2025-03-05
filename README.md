# NPS Night Sky Metrics Report Generator
## Step 1. Installation Guide
1.	Install RStudio (Software Center)
2.	Install R Statistical Software (Software Center)
3.	Install ArcGIS Pro (Software Center)
4.	Install Git (Software Center)
## Step 1a: Preparing Your Workstation (Complete Only Once)
1.	Open a terminal (Git Bash) and navigate to the desired project directory:<br>
>`cd [path to the place where you would like to save the project] `
2.	Clone the GitHub repository:
>`git clone https://github.com/emeyer34/NightSkyMetricsReports.git`
3.	Fetch any updates:
>`git fetch`
4.	Pull the latest changes:
>`git pull origin main`
5.	In Windows Explorer, navigate to the cloned project at:<br>
`NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting` <br>
a.	Open `NightSkyReporting.Rproj`<br>
b.	In the R project, open `NSreportmkdown.Rmd` <br>
c.	Run the code chunk labeled “r packages” on line 54 by pressing the play button on the upper right of the code chunk. This process may take some time if the required packages have not been previously downloaded. <br>
6.	Download the geodatabase from the NSNSD `"Software and Scripts"` folder on SharePoint. This folder will be updated with the latest sALR model, and users will be notified when a new geodatabase is available: <br>
a.	sALR Database <br>
b.	Extract contents of the gdb into the project folder: `NightSkyMetricsReports\NightSkyReportGenerator\ArcPro\NightSkyReportProcess`

## Step 1b: Pull Updates to Workstation (Repeat After Step 1a) <br>
1.	Open a terminal and navigate to the project directory: <br>
>`cd [path to the place where you would like to save the project] ` <br>
2.	Pull the latest updates: <br>
>`git pull` <br>
3.	If "git pull" results in errors due to local modifications, you can overwrite your changes with: <br>
>`git fetch --all `
>`git reset --hard origin/master` 

## Step 2. Spatial analysis and mapping <br>
1.	Ensure you have the latest geodatabase, which will contain the most recent ALR model. NPS employees can find it in the NSNSD SharePoint `Software and Scripts` folder, named `NightSkyReportProcess.gdb.zip`. Extract the contents into: <br> `NightSkyMetricsReports\NightSkyReportGenerator\ArcPro\NightSkyReportProcess`
2.	Open `NightSkyReportProcess.aprx`.<br>
3.	Select the `Processing Map`<br>
4.	In `NightSkyScripts.ipynb`, update the `"repgen"` file path to your local project folder and change the park unit code to the park you are reporting on. Then, select `Run All` in the `Cells` menu.<br> 
5.	In the `ParkOverview` Layout, select the `StudySites` map. Remove any outdated park study sites or boundary layers.<br> 
6.	In `LayoutScripts_ParkOverview`, select `Run All` in the `Cells` menu.<br> 
7.	Return to the `ParkOverview Layout` and refine the map by adjusting labels and zoom levels as needed. Double-click the map title to update the dynamic text to display the Unit_Name from the Park Unit boundary file. When satisfied, export the layout and save it in the park unit folder at:<br> 
`NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting\Figures`.<br>  In the folder of Replace the existing file named `park_geographic_location.PNG`.<br> 
8.	Select the `ALR_PARK` map in the sALR layout. In `LayoutScripts_sALR`, select `Run All` in the `Cells` menu.<br> 
9.	Return to the `sALR layout` and adjust the map to include nearby areas that may influence ALR results. Double-click the map title to update the dynamic text to display the Unit_Name. When satisfied, export the layout and save it in the appropriate park unit folder at: <br> `NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting\Figures`. <br> In the folder of Replace the existing file named `sALR.PNG`.<br> 

## Step 3. Data Exploration<br> 
1.	Navigate to the following location: `NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting`. Open `NightSkyReporting.Rproj`<br> 
2.	Open the RMarkdown document, `NSReportDataExplore.Rmd`. In the Knit dropdown, select `"Knit with Parameters."`<br> 
3.	A data form will appear; enter the park unit code and select `Knit`.<br> 
4.	This will generate an HTML report saved in the same location as the .Rproj file. Use this report to explore the night sky data for the focal park unit. Choose a study site to highlight in the larger published report. It is advised to keep this report open for Step 4.<br> 

## Step 4. Report Generation<br> 
1.	In the same R project as Step 3, open `NSreportmkdown.Rmd`.<br> 
2.	In the Knit dropdown, select `"Knit with Parameters."`<br> 
3.	A data form will appear. Enter the park name and unit code. Accept the default values for the ALR model and census data unless instructed otherwise by the project manager. Use the HTML report from Step 3 to fill out the information for the Site of Interest.<br> 
4.	Click `Knit`. After approximately 5–20 seconds, a Word document will be generated with a fully formatted report. This document will also be saved as `NSreportmkdown.docx` in the same location as the .Rproj.<br> 

## Step 5. Finalize Report<br> 
1.	Move both reports from Steps 3 and 4 to the park folder at: `NightSkyMetricsReports\NightSkyReportGenerator\NightSkyReporting\Parks`<br> 
2.	It is recommended to rename the documents to associate them with the specific park.<br> 
3.	In the Word document, update all the text indicated in bold and noted with "~".<br> 
4.	Once the documents have been finalized and reviewed, they are ready for publication.<br> 

### Public domain

This project is in the worldwide [public domain](LICENSE.md):

> This project is in the public domain within the United States,
> and copyright and related rights in the work worldwide are waived through the
> [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication.
> By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.

