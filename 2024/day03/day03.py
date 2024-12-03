import re
import numpy as np

# Function to check mult()
def get_multiplications(line, regex):
    multiplications_proc = []
    multiplications_line = re.findall(regex, line)
    for mult in multiplications_line:
        multiplications_proc.append([int(num) for num in mult.split(',')])
    return multiplications_proc

multiplications = []
multiplications_do = []
mult_regex = r'mul\((\d{1,3},\d{1,3})\)'
with open('input.txt', 'r') as input_fd:
    for line in input_fd:
        multiplications = multiplications + get_multiplications(line, mult_regex)
        dont_split = line.strip().split("don't()")
        for i, dont_item in enumerate(dont_split):
            if i == 0:
                multiplications_do = multiplications_do + get_multiplications(dont_item, mult_regex)
            else:
                do_split = dont_item.split("do()")
                for i, do_item in enumerate(do_split):
                    if i > 0:
                        multiplications_do = multiplications_do + get_multiplications(do_item, mult_regex)

print(multiplications_do)
print(sum([np.prod(mult) for mult in multiplications]))
print(sum([np.prod(mult) for mult in multiplications_do]))
