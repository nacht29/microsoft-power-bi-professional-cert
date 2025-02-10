# Capstone Project - Executive Data Summary

This is a final course project aimed to showcase my familiarity with operating Microsoft Excel.

It enables me to combine, integrate and solidify the knowledge about Microsoft Excel that I have learned from this course.

## 📚 Table of Contents
- [Back to Excel Basics](#back-to-excel-basics)
- [Skills](skills)
- [Task Summary](#task-summary)
- [Output](#output)
- [Solution](#solution)

### ↩️ Back to Excel Basics
- Click to go **[back to Excel Basics](https://github.com/nacht29/microsoft-power-bi-professional-cert/tree/main/excel-basics)**

### 📊 Skills 
- Generate key business results using a range of formulae, including logical calculations.
- Create percentage calculations which will provide an accurate picture of sales performance.
- Use formatting and worksheet management techniques to make the results suitable for submission to management.

### Task Summary

Prepare an Excel worksheet that presents sales figures for the first quarter of the year and compares said figures to the results for the same period in the previous year. 

This worksheet is called ```Summary``` and is in the workbook ```Quarter One Report.xlsx```. In this worksheet, complete the following actions:

- Create formulas that show the total quarter-one sales for both 2022 and 2023.
- Create formulas that show the percentage increase in sales in 2023. 
- And break down these totals by month with the use of further calculations.

### Output

![image](https://github.com/user-attachments/assets/df6dc78e-78fd-470a-a3b2-f62fbdf323b0)

### Solution

**Steps:**

1. Formatting headers:
	- Add a new column to the left of column E. Select column E, and choose ```Home > Cells > Insert```.

	- Double click on the vertical grid between columns A and B to resize column A and show the data properly.

	- In ```A4``` and ```A10```, add the respective headers: "```TOTAL Q1 SALES```" and "```TOTAL Q1 SALES```". Select ```A4```, choose ```Home > Font > A^``` to enlarge the header by one step and ```Ctrl + B``` to bold the text. Select ```Home > Font > Fill colour (paint icon)``` an apply a background colour to the header in ```A4```.

	- Select ```A4:D4```, then ```Home > Alignment > Merge & Center``` to align the header. 

	- Keeping the highlight, select ```Home > Clipboard > Format Painter (paintbrush icon)```. Select ```A10``` to apply the same formatting for ```A4:D4``` on ```A10:D10```.

	- Select ```B5:D5```, then ```Home > Alignment > Wrap Text``` and ```Ctrl + B``` to make the headings in ```B5:D5``` stand out.

	- Keeping the highlight, select ```Home > Clipboard > Format Painter (paintbrush icon)```. Then, select ```B11:D11``` to apply the same formatting.


2. Completing and customising data visualisation
	- Use ```=PROPER(G2)``` on ```H2``` then use auto-fill to obtain the the ```Product Category``` data in which they are formatted to only have the first words capitalised.
	
	- Select column H, use ```Ctrl + C``` and ```Ctrl +  Alt + V``` and ```ENTER``` to retain the values without the formula. Delete the column G as it is no longer needed for reference.

	- To sort the data by ```Order Date``` in ascending, select ```F2``` column, then ```Ctrl + Shift + End``` to select the data needed to be sorted while excluding the data from columns A to D.

	- Then, select ```Data > Sort & Filter > Sort``` and select ```Order Date``` for the ```Sort by``` drop-down, and make sure ```Order```is set to ```Oldest to Newest```.

	- Columns S to Y are unrelevant to this summary, hence select columns S to Y, right-click and choose ```Hide``` for better readability and to declutter the worksheet.

	- Select ```G2``` and ```View > Window > Freeze Panes > Freeze Panes``` to lock the view for columns A to F, which contains the summary table and ```Product ID```, along with the top row headers.

	- Select column G, go to```Home > Number```, from the drop-down select ```More Number Formats...```. Select ```Date```, and choose the option with the format of ```dd/mm/yyyy```. This formats the ```Order Date``` data to the format of ```dd/mm/yyyy```.

	- Use ```=MONTH(J2)``` and ```=YEAR(J2)``` on ```K2``` and ```L2``` to extract the months and years from the dates. Select ```K2:L2``` and use auto-fill to complete the data ```Month``` and ```Year``` columns.

	- Use ```=N2*O2``` on ```P2``` to calculate the order price before tax. Use auto-fill to complete the data for the ```Total (Before Tax)``` column.

	- Use ```=IF(P2>2000,P2*5%,0)``` on ```Q2``` to assign a tax of 5% of order price if the order total is more than $2000 and 0 if otherwise. Use auto-fill to complete assigning the extra charges, if any.


3. Calculating profit margin
	- On ```B6```, use ```=SUMIF($L$2:$L$246,2022,$R$2:$R$246)```. Copy the formula to ```C6``` and change ```2022``` to ```2023```. This sums up the taxed ordering price for the years 2022 and 2023 separately.
	```=SUMIF($L$2:$L$246,2022,$R$2:$R$246)``` translates to:
		````
		for all values in L2:L216
			if Year = 2022
				sum the value in R2:R246
		````

	- Use ```=SUMIFS($R$2:$R$246,$K$2:$K$246,1,$L$2:$L$246,2022)``` on ```B12``` to calculate the sales for January 2022. The formula summarises as:
		````
		for values K2:K246 = 1 and values L2:L246 = 2022
			sum the values in R2:R246
		````
	Copy the formula for ```B12:B14``` and modify the 3rd argumant, ```1``` to ```2``` for ```February``` and ```3``` for ```March```.

	- Select ```B12:B14```, and copy the formula over to ```C12:C14```. Modify the last argument ```2022``` to ```2023``` to account for January 2023 to March 2023.

	- Use ```=(C6-B6)/B6``` on ```D5``` to calculate the yearly profit margin by using the concept ```(2023 total - 2022 total) / 2022 total```. Copy the formula to ```D12:D14``` to calculate the profit margin for the same month across 2022 and 2023.

#### Feel free to download the Excel file, [````Quarter One Report.xlsx````](https://github.com/nacht29/microsoft-power-bi-professional-cert/blob/main/Excel-Final-Project) for a better view of the end result. The original data is provided in [```Original Workbook.xlsx```](https://github.com/nacht29/microsoft-power-bi-professional-cert/blob/main/Excel-Final-Project)
