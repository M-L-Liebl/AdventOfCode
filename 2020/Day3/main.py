from pathlib import Path

input_array = [[c for c in line] for line in Path("input.txt").read_text().split("\n") if len(line) > 1]
patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def count_tree_encounters(pattern: (int, int)) -> int:
    """
    Counts tree encounters while passing array with given pattern (x, y)
    :param pattern: pattern for traveling through array
    :return: number of tree encounters
    """
    counter = 0
    x = 0
    y = 0
    while y < len(input_array):
        x_max = len(input_array[y])
        if input_array[y][x % x_max] == '#':
            counter += 1
        x = x + pattern[0]
        y = y + pattern[1]
    return counter


print("Solution for task a: ", count_tree_encounters((3, 1)))


allEncounters = 1
for p in patterns:
    allEncounters = allEncounters * count_tree_encounters(p)

print("Solution for task b: ", allEncounters)



