from collections import defaultdict

def solve():
    grid = [line.rstrip("\n") for line in input().splitlines()]
    R = len(grid)
    C = len(grid[0])

    # Find S
    sr = sc = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                sr, sc = r, c
                break
        if sr is not None:
            break

    # dp[col] = number of timelines at this column
    dp = defaultdict(int)
    dp[sc] = 1

    # Process rows below S
    for r in range(sr + 1, R):
        next_dp = defaultdict(int)

        for c, count in dp.items():
            if c < 0 or c >= C:
                continue

            if grid[r][c] == '^':
                next_dp[c - 1] += count
                next_dp[c + 1] += count
            else:
                next_dp[c] += count

        dp = next_dp

        if not dp:
            break

    # Total timelines = sum of all surviving paths
    print(sum(dp.values()))


solve()
