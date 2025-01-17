# Case Study - Contoso Bikes Order Summary

## 📚 Table of Contents
- [Back to Excel Basics](#back-to-excel-basics)
- [Task Summary](#task-summary)
- [Output](#output)
- [Solution](#solution)

### Back to Excel Basics:
- Click to go **[back to Excel Basics](https://github.com/nacht29/microsoft-power-bi-professional-cert/tree/main/excel-basics)**

### Task Summary
Complete a worksheet that contains a summary of the last order placed by Contoso Bikes. 
The worksheet needs the following additional information for Contoso Bikes:

- Delivery charges
- Discount rates
- Regional totals

### Skills
- Logical functions

### Output:

![image](https://github.com/user-attachments/assets/6776d3e8-0ea1-4f68-a760-023049080f23)

### Solution

**Steps:**
- Use ```=IF(G7>10000,10%,0)``` on ```H7``` to assign a 10% percent discount to entries with subtotal > $10,000. Use auto-fill to complete the data for the ```Discount Rate``` column.

- Use ```=IF(H7>0, G7*H7, 0)``` on ```I7``` to calculate the discount amount for the purchases entitled for the 10% discount. The ```IF``` function sets the discount amount to 0, which is shown as a dash "-" in order to avoid inconsistency during calculations. Use auto-fill to complete the data for the ```Discount Amount``` column.

- Use ```=IF(ISNUMBER(I7),G7-I7,G7)``` on ```K7``` to calculate the total price (excluding delivery) by substracting ```Discount Amount``` from ```Subtotal```.
The ```ISNUMBER(I7)``` condition in the ```IF``` function is to avoid calculation inconsistency due to 0 values in ```Discount Amount```.

- Use ```=IFS(J7="A",$D$2,J7="B",$D$3,J7="C",$D$4)``` on ```L7```to assign regional delivery charge to the purchases. Note the absolute cell reference ```$D$2```, ```$D$3``` and ```$D$4``` to keep the reference to regional delivery charges constant. The ```IFS``` function works as summarised below:
	````pseudocode
	if Delivery Region is "A"
		assign Delivery Charge $50
	else if "B"
		assign Delivery Charge $75
	else if "C"
		assign Delivery Charge $100
	````
	Use auto-fill to complete the data for ```Delivery Charge``` column.

- Use ```=K7+L7``` on ```M7``` to calculate the total price, including delivery fee for each purchase. Use auto-fill to complete the data for the ```Total (Including Delivery)``` column.

- Use ```=SUMIF(J7:J16,"A",M7:M16)```, ```=SUMIF(J7:J16,"A",M7:M16)``` and ```=SUMIF(J7:J16,"A",M7:M16)``` for ```Region A```, ```Region B```and ```Region C```to calculate the ```Total Sales by Region```. The formula for ```Region A```summarises as:
	```pseudocode
	scan the range J7:J16
	if Delivery Region is A
		sum the value of Total (Including Delivery)
	```
	The pattern repeats for ```Region B``` and ```Region C```.

#### Feel free to download the Excel file, ````Case Study - Contosso Bikes Order Summary.xlsx```` for a better view of the end result.
