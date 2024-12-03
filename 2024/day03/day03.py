import re
import numpy as np

multiplications = []
with open('input.txt', 'r') as input_fd:
    for line in input_fd:
        multiplications_line = re.findall(r'mul\((\d{1,3},\d{1,3})\)',line)
        for mult in multiplications_line:
            multiplications.append([int(num) for num in mult.split(',')])

print(sum([np.prod(mult) for mult in multiplications]))
