def can_form(test_value, nums):
    """
    Recursively checks if it's possible to form test_value by
    inserting '+' or '*' between the numbers in nums.
    """
    # Base case: if there's only one number left, check if it equals test_value.
    if len(nums) == 1:
        return nums[0] == test_value

    # Split the list into the first two numbers and the rest.
    a, b, *rest = nums
    # Try using addition:
    if can_form(test_value, [a + b] + rest):
        return True
    # Try using multiplication:
    if can_form(test_value, [a * b] + rest):
        return True
    # Try using appendation
    if can_form(test_value, [int((str(a)+str(b)))]+rest):
        return True

    return False


def solve(input_text):
    """
    Processes the input, where each line is of the format:
    'target: num1 num2 num3 ...'
    Returns the sum of the target numbers for which a valid operator insertion exists.
    """
    total = 0
    for line in input_text.strip().splitlines():
        if not line.strip():
            continue  # skip empty lines
        # Split the line into the target and the numbers
        target_str, nums_str = line.split(":")
        target = int(target_str.strip())
        nums = [int(x) for x in nums_str.strip().split()]
        # If the equation can be made to equal the target, add the target to the total.
        if can_form(target, nums):
            total += target
    return total


if __name__ == "__main__":
    # Here's the sample input from the problem description.
    with open("input.txt", "r") as f:
        input_data = f.read()
    result = solve(input_data)
    print("Total calibration result:", result)

