import sys

def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    accessible = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            adj = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        adj += 1

            if adj < 4:
                accessible += 1

    return accessible


def main():
    grid = [line.rstrip('\n') for line in sys.stdin if line.strip() != '']
    result = count_accessible_rolls(grid)
    print(result)


if __name__ == "__main__":
    main()
