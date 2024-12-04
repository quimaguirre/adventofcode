import re

#### PART 1 ####

# Based on: https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python

matrix = []
with open('input.txt') as input_fd:
    for line in input_fd:
        matrix.append(line.strip())

max_row = len(matrix[0])
max_col = len(matrix)

# Get all columns, rows and forward/backwards diagonals
matrix_lines = {}
matrix_lines["cols"] = [[] for _ in range(max_col)]
matrix_lines["rows"] = [[] for _ in range(max_row)]
matrix_lines["fdiag"] = [[] for _ in range(max_row + max_col - 1)]
matrix_lines["bdiag"] = [[] for _ in range(len(matrix_lines["fdiag"]))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        matrix_lines["cols"][x].append(matrix[y][x])
        matrix_lines["rows"][y].append(matrix[y][x])
        matrix_lines["fdiag"][x + y].append(matrix[y][x])
        matrix_lines["bdiag"][x - y - min_bdiag].append(matrix[y][x])

# Iterate through each type of line and search for the substring XMAS or SAMX
xmas_counts = 0

for type_line in matrix_lines.keys():
    for line in matrix_lines[type_line]:
        line = ''.join(line)
        xmas_counts += line.count('XMAS')
        xmas_counts += line.count('SAMX')

print(xmas_counts)


#### PART 2 ####

# Iterate through each row, search for the indexes of 'A's, and then check the
# two diagonals to see if the substrings 'MAS' or 'SAM' are there
xmas_counts2 = 0

for i, line in enumerate(matrix_lines["rows"]):
    if i > 0 and i < (max_row - 1):
        substring_indexes = [m.start() for m in re.finditer('(?=A)', ''.join(line))]
        for substring_index in substring_indexes:
            if substring_index > 0 and substring_index < (max_col - 1):
                upper_back = matrix_lines["rows"][i - 1][substring_index - 1]
                lower_fwd = matrix_lines["rows"][i + 1][substring_index + 1]
                upper_fwd = matrix_lines["rows"][i - 1][substring_index + 1]
                lower_back = matrix_lines["rows"][i + 1][substring_index - 1]
                diag1 = ''.join([upper_back, 'A', lower_fwd])
                diag2 = ''.join([upper_fwd, 'A', lower_back])
                if diag1 in ['MAS', 'SAM'] and diag2 in ['MAS', 'SAM']:
                    xmas_counts2 += 1

print(xmas_counts2)
