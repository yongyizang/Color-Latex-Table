# Color Latex Table
 Easily color your LaTeX tables based on their corresponding values.
 Color Latex Table contains a simple python script. Just paste your existing LaTeX table in.

## Documentation
See `color_latex_table.py` - configuration should be quite straight forward.

For each table cell, we can set its text color and cell color (background color). We assume these values are determined by the number within that cell.

To change the coloration rule, change the definition of `coloration(number)`. Set `min_value` and `max_value` to determine the minimum and maximum values on the scale of the numbers you want to color.

This script is not very throughly tested; However, it seems to work with \textbf text in cells.