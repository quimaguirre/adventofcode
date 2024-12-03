import re
import numpy as np

multiplications = []
multiplications_do = []
with open('input.txt', 'r') as input_fd:
    for line in input_fd:
        multiplications_line = re.findall(r'mul\((\d{1,3},\d{1,3})\)', line)
        for mult in multiplications_line:
            multiplications.append([int(num) for num in mult.split(',')])
        dont_split = line.strip().split("don't()")
        for i, dont_item in enumerate(dont_split):
            if i == 0:
                multiplications_item = re.findall(r'mul\((\d{1,3},\d{1,3})\)', dont_item)
                for mult in multiplications_item:
                    multiplications_do.append([int(num) for num in mult.split(',')])
            else:
                do_split = dont_item.split("do()")
                for i, do_item in enumerate(do_split):
                    if i > 0:
                        multiplications_item = re.findall(r'mul\((\d{1,3},\d{1,3})\)', do_item)
                        for mult in multiplications_item:
                            multiplications_do.append([int(num) for num in mult.split(',')])

print(multiplications_do)
print(sum([np.prod(mult) for mult in multiplications]))
print(sum([np.prod(mult) for mult in multiplications_do]))
