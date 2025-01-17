# Intro to Power BI

## Summary

This is my first time exploring Power BI. 

I created some simple visuals to show the sales condition of different bicycles by category, size and sales amount.

## Output

![Image](https://github.com/user-attachments/assets/a67a1dd3-0d8b-488f-8d6d-1daeb11b5e4b)

## Steps:
- Load CSV data and establish connection.

- Enable ```View > Snap to Grid``` to ensure proper alignment.

- Create a slicer named ```Product Category``` and add ```Product Category``` data to ```Field```.

- Create a slicer named ```Payment Method``` and add ```Payment Method``` data to ```Field```.\

- Create a ring chart ```Order Total by Product Category``` to show the sales of each product category. The title is named, boldened and enlarged in ```Vizualisations > Format your visual > General > Title```.

- Add ```Sum of Order Total``` to ```Value``` and ```Product Category``` to ```Details```.

- Adjust the colour scheme for the ring chart, as shown in the output.

- Create a horizontal stacked bar chart to show the sales of products by size for each category: ```Order Total by Product Size and Product Category for 2023```. The title is named, boldened and enlarged in ```Vizualisations > Format your visual > General > Title```.

- Add ```Product Size``` to ```Y-Axis``` and ```Sum of Total Order``` to ```X-Axis``` and ```Product Category``` to ```Legend```. Go to ```Vizualisations > Format your visual > Visuals``` and enable ```Zoom Slider``` to enable users to zoom into a specific axis and inspect a particular category or size and their corresponding sales.

- For all assets, go to ```Vizualisations > Format your visual > General > Title > Effects```. Then, go to and enable ```Shadows``` and set ```Offset``` to ```Center```.