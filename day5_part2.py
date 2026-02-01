def count_fresh_ids_from_ranges():
    ranges = []

    # Read ranges until blank line
    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line == "":
            break

        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    if not ranges:
        print(0)
        return

    # Sort ranges by start
    ranges.sort()

    total = 0
    curr_start, curr_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= curr_end + 1:   # overlap or touching
            curr_end = max(curr_end, end)
        else:
            total += curr_end - curr_start + 1
            curr_start, curr_end = start, end

    # add last range
    total += curr_end - curr_start + 1

    print(total)


# Run
count_fresh_ids_from_ranges()
