import re
import numpy as np

# Function to check a multiplication regex within a line and process it
def get_multiplications(line, regex):
    multiplications_proc = []
    multiplications_line = re.findall(regex, line)
    for mult in multiplications_line:
        multiplications_proc.append([int(num) for num in mult.split(',')])
    return multiplications_proc

multiplications = []
multiplications_do = []
dont_status = False # Initialize don't status
mult_regex = r'mul\((\d{1,3},\d{1,3})\)'
with open('input.txt', 'r') as input_fd:
    for line in input_fd:
        multiplications = multiplications + get_multiplications(line, mult_regex)
        # Split by don't
        dont_split = line.strip().split("don't()")
        for i, dont_item in enumerate(dont_split):
            # Check first part of split (before don't) making sure that the
            # don't status is False (as it could still be active from previous
            # lines)
            if i == 0 and dont_status == False:
                multiplications_do = multiplications_do + get_multiplications(dont_item, mult_regex)
            else:
                dont_status = True
                # Split by do's now, the item before the do is skipped and the
                # rest are considered
                do_split = dont_item.split("do()")
                for j, do_item in enumerate(do_split):
                    if j > 0:
                        dont_status = False
                        multiplications_do = multiplications_do + get_multiplications(do_item, mult_regex)

print(sum([np.prod(mult) for mult in multiplications]))
print(sum([np.prod(mult) for mult in multiplications_do]))
