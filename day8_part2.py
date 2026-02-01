import sys

def solve():
    points = []
    for line in sys.stdin:
        if line.strip():
            x, y, z = map(int, line.strip().split(","))
            points.append((x, y, z))

    n = len(points)

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            d = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            edges.append((d, i, j))

    edges.sort()

    last_i = last_j = None
    unions = 0

    for _, i, j in edges:
        if union(i, j):
            last_i, last_j = i, j
            unions += 1
            if unions == n - 1:
                break

    x1 = points[last_i][0]
    x2 = points[last_j][0]
    print(x1 * x2)

solve()
