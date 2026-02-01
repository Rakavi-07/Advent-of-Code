def count_fresh_from_input():
    ranges = []
    ingredients = []

    reading_ranges = True

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line == "":
            reading_ranges = False
            continue

        if reading_ranges:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            ingredients.append(int(line))

    fresh_count = 0

    for ing in ingredients:
        for start, end in ranges:
            if start <= ing <= end:
                fresh_count += 1
                break

    print(fresh_count)


# Run
count_fresh_from_input()
