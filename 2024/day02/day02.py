# Read input data frame
safe_num = 0
safe_num_with_removal = 0

# Function to check safety in levels
def check_levels(levels):
    # Calculate difference between consecutive levels
    diff_levels = [int(x) - int(levels[i - 1]) for i, x in enumerate(levels) if i > 0]
    # Check 1: All have same sign
    same_sign = all(item > 0 for item in diff_levels) or all(item < 0 for item in diff_levels)
    # Check 2: Absolute increase between 1 and 3
    controlled_increase = all((abs(item) >= 1 and abs(item) <= 3) for item in diff_levels)
    if same_sign and controlled_increase:
        return True
    else:
        return False

with open('input.txt', 'r') as input_fd:
    for line in input_fd:
        levels = line.strip().split()
        safety = check_levels(levels)
        if safety:
            safe_num += 1
            safe_num_with_removal += 1
        else:
            # Check safety after removing 1 level
            for i in range(len(levels)):
                new_levels = [item for j, item in enumerate(levels) if j != i]
                new_safety = check_levels(new_levels)
                if new_safety:
                    safe_num_with_removal += 1
                    break

print(safe_num)
print(safe_num_with_removal)
