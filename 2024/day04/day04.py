# Based on: https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python

matrix = []
with open('input.txt') as input_fd:
    for line in input_fd:
        matrix.append(line.strip())

max_row = len(matrix[0])
max_col = len(matrix)

cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(matrix[y][x])
        rows[y].append(matrix[y][x])
        fdiag[x+y].append(matrix[y][x])
        bdiag[x-y-min_bdiag].append(matrix[y][x])

horizontal_straight = 0
horizontal_backwards = 0
vertical_straight = 0
vertical_backwards = 0
fdiag_straight = 0
fdiag_backwards = 0

for row in rows:
    row = ''.join(row)
    horizontal_straight += row.count('XMAS')
    horizontal_backwards += row.count('SAMX')

print(horizontal_straight)
print(horizontal_backwards)

for col in cols:
    col = ''.join(col)
    vertical_straight += col.count('XMAS')
    vertical_backwards += col.count('SAMX')

print(vertical_straight)
print(vertical_backwards)
