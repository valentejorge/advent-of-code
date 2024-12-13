with open('puzzle.txt', 'r') as puzzle:
    puzzle = puzzle.read()
    print(f'puzzle:\n{puzzle.splitlines()[:10]}')
    right = puzzle.split()[1::2]
    left = puzzle.split()[0::2]

    right_sorted = sorted(right)
    left_sorted = sorted(left)

    print(f'left:\n{left[0:10]}')
    print(f'right:\n{right[0:10]}')
    print(f'left:\n{left_sorted[0:10]}')
    print(f'right:\n{right_sorted[0:10]}')

    result = []

    for i in range(1000):
        print(i)
        result.append(
                abs(int(right_sorted[i]) - int(left_sorted[i]))
        )
    print(result)
    total_distance = sum(result)
    print(total_distance)
