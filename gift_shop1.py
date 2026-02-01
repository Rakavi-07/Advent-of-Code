def is_invalid_id(n: int) -> bool:
    """
    Part 2 rule:
    n is invalid if its decimal representation is composed of
    some digit block repeated at least twice.
    Example invalid:
      11 (1*2), 111 (1*3), 1010 (10*2), 824824824 (824*3)
    """
    s = str(n)
    L = len(s)

    # Try all possible block lengths
    for block_len in range(1, L // 2 + 1):
        if L % block_len != 0:
            continue  # total length must be multiple of block_len

        repeats = L // block_len
        if repeats < 2:
            continue  # must repeat at least twice

        block = s[:block_len]
        if block * repeats == s:
            return True  # found a repeating pattern

    return False  # no repeating pattern found


def main():
    import sys

    # Read the single long line with all ranges
    line = sys.stdin.readline().strip()

    total = 0  # sum of all invalid IDs

    # Split ranges by comma: "11-22,95-115,..."
    ranges = line.split(',')

    for part in ranges:
        part = part.strip()
        if not part:
            continue

        start_str, end_str = part.split('-')
        start = int(start_str)
        end = int(end_str)

        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n

    print(total)


if __name__ == "__main__":
    main()
