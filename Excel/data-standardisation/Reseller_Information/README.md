# Case Study - Reseller Information

## 📚 Table of Contents
- [Back to Excel Basics](#back-to-excel-basics)
- [Task Summary](#task-summary)
- [Output](#output)
- [Solution](#solution)

### Back to Excel Basics:
- Click to go **[back to Excel Basics](https://github.com/nacht29/microsoft-power-bi-professional-cert/tree/main/excel-basics)**

### Task Summary
- Update a spreadsheet called ````Reseller Details```` that records details of Adventure Work’s resellers in the United States.
- This information in the spreadsheet was downloaded from another system. The download process created several inconsistencies or errors within the data.
- These errors include unnecessary spaces, the use of the wrong case, and entries that need to be joined together or split apart.
-  Standardise the data so that it can be used for analysis.

### Skills
- Excel functions and formula
- Data standardisation

### Output:

![image](https://github.com/user-attachments/assets/9df28cd0-74ba-4126-85fe-f21fef05d27d)

### Solution

**Steps:**
- Use ````=TRIM(B2)```` in ````C2```` to trim empty spaces in the reseller's name. Use auto-fill to complete the  ````Reseller Name```` column.

- Use ````=PROPER(D2)```` to obtain ````City```` name for each entry with only the first letter of every word capitalised. Use auto-fill to complete the ````City```` column.

- In ````I2````, use the formula ````=LEFT(H2, 6)```` to extract the word "States". Use auto-fill to complete column I.

- In ```J2```, use ```=RIGHT(H2, 8)``` to extract the word "New York". Use auto-fill to complete the ```Head Office``` column.

- In ```K2```, use the formula ````=CONCAT(G2," ",I2)```` to complete the country name ````United States````. Use autofill to complete the ```Country``` column.

- In ```L2```, use ```=MID(H2, 8, 3)``` to to extract the words "uSA". Then, in ```M2```, use ```=UPPER(L2)``` to capitalise the value in L2. Select ```M2:L2``` and use auto-fill to complete the ```Region``` column.

- Use auto-fill and```Ctrl+C``` to copy the values of the following cells and their subsequent cells and select ```Paste Values``` from the ```Paste``` dropdown in the ```Home``` tab in the respective pairs:

	Format: ```<cell to auto-fill and copy> - <cell to paste>```
	```C2 - C2```, ```E2- E2```, ```J2 - J2```, ```K2 - K2```, ```M2 - M2```

- The point above is to prepare to delete columns which serves as reference, such as ```B2``` which is used in ```C2```. We want to retain the values in the columns we just used copy and paste on and avoid the ```#REF!``` error.

#### Feel free to download the Excel file, ````Case Study - Reseller Information```` for a better view of the end result.
