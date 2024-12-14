def solve_puzzle(puzzle):
    right = sorted(puzzle.split()[1::2])
    left = sorted(puzzle.split()[0::2])

    result = []

    for i in range(1000):
        result.append(
                int(right[i]) * int(left[i])
        )

    return sum(result)


with open('puzzle2.txt', 'r') as f:
    puzzle = f.read()

    print(solve_puzzle(puzzle))
