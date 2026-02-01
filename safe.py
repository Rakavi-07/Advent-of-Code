import sys

position = 50      # starting point
zero_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    dir_ = line[0]          # 'L' or 'R'
    value = int(line[1:])   # number after it

    if dir_ == 'L':
        position = (position - value) % 100
    elif dir_ == 'R':
        position = (position + value) % 100
    else:
        continue  # ignore bad lines

    if position == 0:
        zero_count += 1

print(zero_count)
