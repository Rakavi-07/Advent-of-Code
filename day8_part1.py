import sys
from collections import Counter

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
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            d = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            edges.append((d, i, j))

    edges.sort()

    # EXACTLY 1000 closest PAIRS
    for i in range(1000):
        _, a, b = edges[i]
        union(a, b)

    comps = Counter(find(i) for i in range(n))
    sizes = sorted(comps.values(), reverse=True)

    print(sizes[0] * sizes[1] * sizes[2])

solve()
