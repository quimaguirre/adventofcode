# Read input data frame
safe_num = 0
with open('input.txt', 'r') as input_fd:
    for line in input_fd:
        levels = line.strip().split()
        diff_levels = [int(x) - int(levels[i - 1]) for i, x in enumerate(levels) if i > 0]
        # Check 1: All have same sign
        same_sign = all(item > 0 for item in diff_levels) or all(item < 0 for item in diff_levels)
        # Check 2: Absolute increase between 1 and 3
        controlled_increase = all((abs(item) >= 1 and abs(item) <= 3) for item in diff_levels)
        if same_sign and controlled_increase:
            safe_num += 1

print(safe_num)
