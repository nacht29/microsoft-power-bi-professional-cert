# Case Study - Revenue Figures

## 📚 Table of Contents
- [Task Summary](#task-summary)
- [Output](#output)
- [Solution](#solutions)

### Task Summary
Aimee at Adventure Works has asked you to help her prepare an Excel file that she will present at a management team financial review meeting. The worksheet tracks the items sold by one of Adventure Work’s divisions. The file needs to contain results such as costs, revenue, and profit. Your task is to create the formulas and calculations for this sheet.

### Output

#### Original Data:
![image](https://github.com/user-attachments/assets/11327420-e4c5-4101-af91-98a7b2c194ed)

#### Final result:
![image](https://github.com/user-attachments/assets/e512ec42-a7a1-4959-bd25-b7313c780772)

### Solution

**Steps:**

- Use the formula ````=E4*F4```` in cell ````G4```` to calculate the ````Purchase Cost````. Use auto-fill to complete calculation in column G.

- Use the formula ````=F4*$P$1```` to calculate the ````Shipping Cost```` for ````F4````. Use auto-fill to complete calculation for column F. Note that absolute cell reference ````$P$1```` to ````P1```` to ensure ````Shipping rate (per item)```` stays constant when using auto-fill.

- Use the formula ````=G4+H4```` on ````I4````. This sums the total ````Purchase Cost```` and total ````Shipping Cost```` to calculate the ````Total Costs```` of purchasing all of each entry's item. Use auto-fill to complete the data in column I.

- Use the formula ````=(I4/F4)*1.5```` on ````J4```` to calculate the retail price for each item. In the case study it is stated the retail price must ensure a profit of 50% from the total cost for each item.

- In continuation to the point above: use ````(I4/F4)```` to divide the ````Total Costs```` by ````Items Purchased```` to obtain the cost of one item. Then, multiply the value by 1.5 to calculate the retail price to include the extra 50% markup.

- Use the formula ````=J4*K4```` on ````L4```` to calculate the ````Total Revenue```` for each entry by multiplying the retail price per unit and items sold. Complete the data in column L with autofill.

- Use the formula ````=L80-I80```` on ````M4```` to calculate the ````Profit```` for each entry by subtracting the ````Total Costs```` from ````Revenue```` for each entry. Complete the data in column M with autofill.

- Use the formula ````=SUM(G4:G200)```` on ````G201```` to sum up the ````Purchase Cost```` of all entries. Use autofill on ````G201:M201```` to sum up the ````Shipping Costs````, ````Total Costs````, ````Retail Price (per unit)````, ````Items Sold````, ````Revenue```` and ````Profit```` for all entries.

- To calculate ````Profit```` as in total profit for ````O2````, simply use ````=M201```` in ````P3```` to refer to the cell that contains the value for the sum of profits.

- To calculate ````Profit Margin```` for ````O3````, use ````=M201/L201```` on ````P3````, then format the cell data type to percentage. This gives the profit as a percentage of the total cost:

	````profit margin = profit/total cost * 100%````.

#### Feel free to download the Excel file, ````Case Study - Revenue Figures```` for a better view of the end result.