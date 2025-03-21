# TODO: FIX THIS AND GET THE SAME RESULT AS IN gpt.py
with open("input.txt", "r") as f:
    data = f.readlines()

equations: dict[int, list[int]] = {}

for item in data:
    splitted = item.split(":")
    equations[int(splitted[0])] = [int(item) for item in splitted[1].strip().split(" ")]

working = []
# possible operators are * (True) and + (False)

"""
for result in equations.keys():
    n = len(equations[result])-1
    combinations = 1 << n
    combinate = []

    for i in range(combinations):
        combs = [(i >> j) & 1 == 1 for j in range(n)]
        combinate.append(combs)

    for item in combinate:
        subtotal = 0
        for index, sub in enumerate(equations[result]):
            if index == 0:
                subtotal = sub
                continue
            if item[index-1]:
                subtotal *= sub
                continue
            else:
                subtotal += sub
                continue
        if subtotal == result:
            working.append(result)
            break

print(sum(working))

"""

def canGenerateResult(currSum, idx, result, equation):
    if idx == len(equation):
        if currSum == result:
            return True
        else:
            return False
    return (canGenerateResult(currSum + equation[idx], idx + 1, result, equation) or
            canGenerateResult(currSum * equation[idx], idx + 1, result, equation))


def calibrationResult(equations: dict) -> int:
    totalCalibrationResult = 0
    for result, equation in equations.items():
        if canGenerateResult(equation[0], 1, result, equation):
            totalCalibrationResult += result
    return totalCalibrationResult

print(calibrationResult(equations))
