def combinations(items, n):
    """
    Generates all combinations of n items from a given list.

    Args:
        items: The list of items to choose from.
        n: The number of items to include in each combination.

    Returns:
        A list of lists, where each inner list is a combination of n items.
    """

    if n == 0:
        return [[]]  # Base case: if n is 0, return a list containing an empty list

    if not items:
        return []  # Base case: if items is empty, return an empty list

    first = items[0]
    rest = items[1:]

    combinations_with_first = [
        [first] + combo for combo in combinations(rest, n - 1)
    ]
    combinations_without_first = combinations(rest, n)

    return combinations_with_first + combinations_without_first

def uniqueantinodes(poses: dict, data: list[list[str]]) -> int:
    antinodes = []
    for val in poses.values():
        combs = combinations(val, 2)
        for item in combs:
            vec = [item[0][0]-item[1][0], item[0][1]-item[1][1]]
            antinodes.append([item[0][0]+vec[0], item[0][1]+vec[1]])
            antinodes.append([item[1][0]-vec[0], item[1][1]-vec[1]])
    new = []
    for item in antinodes:
        if item not in new and item[0] >= 0 and item[1] >= 0 and item[0] < len(data) and item[1] < len(data[0]):
            new.append(item)
    return len(new)

with open("input.txt", "r") as f:
    d = f.readlines()

data = [list(i.strip()) for i in d]

poses = {}

for lindex, line in enumerate(data):
    for iindex, item in enumerate(line):
        if item != '.':
            if item in poses.keys():
                poses[item].append([lindex, iindex])
                continue
            poses[item] = [[lindex, iindex]]
            continue

print(uniqueantinodes(poses, data))

