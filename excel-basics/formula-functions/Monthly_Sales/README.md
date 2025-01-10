# Case Study - Monthly Sales Report

## 📚 Table of Contents
- [Task Summary](#task-summary)
- [Output](#output)
- [Solution](#solution)

### Task Summary
- Create an Excel worksheet that tracks the sales results for one of Adventure Works' most popular products, the A2Mountain Bike Frame.

#### Skills:
- Excel functions and formula

### Output:

![image](https://github.com/user-attachments/assets/73d0f3b7-7a69-4cdb-ace2-f7e70ed7ec75)

### Solution

**Steps:**
- Use the formula ````=C4*D4```` to calculate the daily revenue. Use auto-fill to complete the data in the ````Total```` column.

- Use ````=SUM(C4:C33)```` on ````C35```` to calculate the monthly revenue by summing up the daily revenue from ````Total```` column.

- Use ````=SUM(C4:C33)```` on ````C36```` to calculate total unit sold in month by summing up the daily sales entry from ````Number of Units Sold````.

- Use ````=MIN(C4:C33)```` and ````=MAX(C4:C33)```` to find the minimum and maximum sales in the month.

- Use ````=COUNTA(B4:B33)```` to calculate the number of entries in the ````Days```` column. It is important to use ````COUNTA```` instead of ````COUNT```` because ````COUNT```` only takes into account numeric entries, hence none of the date entries will be recorded and ````Days In Month```` will be 0.

- Use ````=AVERAGE(E4:E33)```` to calculate the average value from te ````Total```` column to obtain the daily revenue in the month.

#### Feel free to download the Excel file, ````Case Study - Monthly Sales Report```` for a better view of the end result.
