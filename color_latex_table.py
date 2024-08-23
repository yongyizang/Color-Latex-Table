import re
min_value = 0
max_value = 100

def clamp(value, min_value, max_value):
    """ output a value that sees min_value as 0, max_value as 1 """
    return (value - min_value) / (max_value - min_value)

def coloration(number):
    number = clamp(number, min_value, max_value)
    # 0.3 changes when text becomes white.
    if number < 0.3:
        number = 1 - number
        output_rgb = (255*number, 255*number, 255*number)
        text_rgb = (0, 0, 0)
    else:
        number = 1 - number
        output_rgb = (255*number, 255*number, 255*number)
        text_rgb = (255, 255, 255)
    return output_rgb, text_rgb

def process_latex_line(line):
    cell_pattern = re.compile(r'([^&\\\\]+)(?=&|\\\\)')
    
    def modify_cell(match):
        cell_content = match.group(1).strip()
        try:
            if "textbf{" in cell_content:
                temp_cell_content = cell_content[cell_content.index("{")+1:cell_content.index("}")]
            else:
                temp_cell_content = cell_content
            
            # Extract the first number before +, - and ± symbol
            number_match = re.match(r'(-?\d+(?:\.\d+)?)\s*±', temp_cell_content)
            if number_match:
                number = float(number_match.group(1))
            else:
                # If no ± symbol, try to convert the whole content to float
                number = float(temp_cell_content)

            if min_value <= number <= max_value:
                bg_color, text_color = coloration(number)
                cell_content = r'\cellcolor[rgb]{{{:.2f},{:.2f},{:.2f}}} \textcolor[rgb]{{{:.2f},{:.2f},{:.2f}}}{{{}}}'.format(
                    bg_color[0]/255, bg_color[1]/255, bg_color[2]/255,
                    text_color[0]/255, text_color[1]/255, text_color[2]/255,
                    cell_content
                )
        except ValueError:
            pass
        
        return cell_content

    line = cell_pattern.sub(modify_cell, line)
    line = line.replace('&', ' & ')
    line = line.replace("\\\\cellcolor", "\\cellcolor")
    line = line.replace("\\\\textcolor", "\\textcolor")
    line = line.replace('\\\\', ' \\\\ ')
    return line

def process_latex_table(latex_table):
    new_lines = []
    for line in table2lines(latex_table):
        if isCellLine(line):
            line = process_latex_line(line)
        new_lines.append(line)
    modified_table = '\n'.join(new_lines)
    return modified_table

def table2lines(table):
    lines = table.split('\n')
    return lines

def isCellLine(line):
    return ('&' in line) and ('\\' in line)

if __name__ == '__main__':
    print("LaTex Coloration Helper.\n")
    latex_table = r"""
    Paste your latex table here!
    """
    print(process_latex_table(latex_table))
