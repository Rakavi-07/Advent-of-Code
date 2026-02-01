max_area = 0
best = None

for i in range(len(red_tiles)):
    r1, c1 = red_tiles[i]
    for j in range(i+1, len(red_tiles)):
        r2, c2 = red_tiles[j]

        if r1 == r2 or c1 == c2:
            continue

        top = min(r1, r2)
        bottom = max(r1, r2)
        left = min(c1, c2)
        right = max(c1, c2)

        # check ONLY interior tiles
        if top + 1 <= bottom - 1 and left + 1 <= right - 1:
            if invalid_sum(top + 1, left + 1, bottom - 1, right - 1) != 0:
                continue

        area = (bottom - top + 1) * (right - left + 1)
        if area > max_area:
            max_area = area
            best = ((r1, c1), (r2, c2))
            print("ANSWER:", max_area)
            print("Best rectangle corners:", best)
