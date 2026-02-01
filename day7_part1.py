def solve():
    grid = [list(line.rstrip("\n")) for line in input().splitlines()]
    R = len(grid)
    C = len(grid[0])

    # Find S
    start_r = start_c = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                start_r, start_c = r, c
                break
        if start_r is not None:
            break

    if start_r is None:
        print("S not found")
        return

    beams = {start_c}
    splits = 0

    # Start from the row BELOW S
    for r in range(start_r + 1, R):
        next_beams = set()

        for c in beams:
            if c < 0 or c >= C:
                continue

            if grid[r][c] == '^':
                splits += 1
                next_beams.add(c - 1)
                next_beams.add(c + 1)
            else:
                next_beams.add(c)

        beams = next_beams
        if not beams:
            break

    print(splits)


solve()
