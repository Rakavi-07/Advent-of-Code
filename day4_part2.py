import sys

# 8 neighboring directions (row, col offsets)
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def count_adjacent_rolls(grid, r, c):
    """Count how many of the 8 neighbors of (r, c) are '@' rolls."""
    rows = len(grid)
    cols = len(grid[0])
    adj = 0

    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                adj += 1

    return adj


def simulate_removal(grid):
    """
    Repeatedly:
      - find all '@' with < 4 neighboring '@'
      - remove them all at once
    Return total number of rolls removed.
    """
    rows = len(grid)
    cols = len(grid[0])

    # Convert strings to list of chars so we can modify them
    g = [list(row) for row in grid]

    total_removed = 0

    while True:
        to_remove = []

        # Find all accessible rolls in the current grid
        for r in range(rows):
            for c in range(cols):
                if g[r][c] != '@':
                    continue
                adj = count_adjacent_rolls(g, r, c)
                if adj < 4:
                    to_remove.append((r, c))

        # If none found, we are done
        if not to_remove:
            break

        # Remove them all simultaneously
        for r, c in to_remove:
            g[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed


def main():
    # Read grid from stdin, ignore empty lines
    grid = [line.rstrip('\n') for line in sys.stdin if line.strip() != '']

    result = simulate_removal(grid)
    print(result)


if __name__ == "__main__":
    main()
