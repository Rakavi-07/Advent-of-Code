def solve():
    lines = [line.rstrip("\n") for line in input().splitlines()]
    if not lines:
        print(0)
        return

    height = len(lines)
    width = max(len(line) for line in lines)

    # Pad lines to equal width
    grid = [line.ljust(width) for line in lines]

    total = 0
    col = 0

    while col < width:
        # Skip empty columns
        if all(grid[row][col] == " " for row in range(height)):
            col += 1
            continue

        # Collect one problem block
        cols = []
        while col < width and not all(grid[row][col] == " " for row in range(height)):
            cols.append(col)
            col += 1

        # Extract numbers and operator
        numbers = []
        operator = None

        for row in range(height):
            token = "".join(grid[row][c] for c in cols).strip()
            if not token:
                continue
            if token in "+*":
                operator = token
            else:
                numbers.append(int(token))

        # Compute result
        if operator == "+":
            result = sum(numbers)
        else:  # '*'
            result = 1
            for n in numbers:
                result *= n

        total += result

    print(total)


solve()
