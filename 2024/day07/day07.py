def use_operator(num1, num2, operator):
    print(f"operation: {num1} {operator} {num2}")
    if operator == '*':
        return num1 * num2
    else:
        return num1 + num2

def calculate_equation(nums):
    results = []
    for i in range(len(nums)):
        if i < len(nums) - 1:
            for op in ['*', '+']:
                results.append(use_operator(nums[i], nums[i+1], op))
    return results

def get_list_of_operators(k, operators_list = []):
    if k > 1:
        for op in ['*', '+']:
            print(f"Iteration: {k}. Op: {op}")
            operators_list.append(op)
            return get_list_of_operators(k - 1, operators_list)
    else:
        for op in ['*', '+']:
            print(f"Iteration: {k}. Op: {op}")
            operators_list.append(op)
        return operators_list

def recurse(nums, k):
    if(k > 0):
        return recurse(nums, k - 1)
    else:
        return calculate_equation(nums)

with open('small_input.txt') as input_fd:
    for line in input_fd:
        equation = line.strip().split(': ')
        expected_result = equation[0]
        nums = [int(x) for x in equation[1].split(' ')]
        num_operators = len(nums) - 1
        operators_list = get_list_of_operators(num_operators)
        print(f"Num operators: {num_operators}. List: {operators_list}")
        #results = recurse(nums, num_operators)
        #print(f"Input list: {nums}. Expected result: {expected_result}. Results: {results}")

