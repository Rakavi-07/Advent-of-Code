import sys

position = 50      # dial starts at 50
zero_count = 0     # count every click that lands on 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    direction = line[0]
    value = int(line[1:])

    step = 1 if direction == 'R' else -1

    # simulate click-by-click
    for _ in range(value):
        position = (position + step) % 100
        if position == 0:
            zero_count += 1

print(zero_count)
