def solve():
    lines = [line.rstrip("\n") for line in input().splitlines()]
    if not lines:
        print(0)
        return

    height = len(lines)
    width = max(len(line) for line in lines)

    grid = [line.ljust(width) for line in lines]

    total = 0
    col = width - 1  # start from RIGHT

    while col >= 0:
        # skip empty columns
        if all(grid[row][col] == " " for row in range(height)):
            col -= 1
            continue

        # collect one problem block (right → left)
        cols = []
        while col >= 0 and not all(grid[row][col] == " " for row in range(height)):
            cols.append(col)
            col -= 1

        numbers = []
        operator = None

        for row in range(height):
            # 🔥 FIX: reverse cols so digits are MSB → LSB
            token = "".join(grid[row][c] for c in reversed(cols)).strip()
            if not token:
                continue
            if token in "+*":
                operator = token
            else:
                numbers.append(int(token))

        if operator == "+":
            total += sum(numbers)
        else:
            result = 1
            for n in numbers:
                result *= n
            total += result

    print(total)


solve()
