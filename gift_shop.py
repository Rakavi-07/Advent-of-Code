def is_invalid_id(n: int) -> bool:
    """
    Return True if n is an 'invalid' ID:
    - its decimal representation has even length
    - and it is formed by a sequence repeated twice (like 123123).
    """
    s = str(n)
    if len(s) % 2 != 0:  # odd length -> cannot be X+X
        return False

    half = len(s) // 2
    return s[:half] == s[half:]  # first half == second half


def main():
    import sys

    # Read the whole line with all ranges (e.g. 11-22,95-115,...)
    line = sys.stdin.readline().strip()

    total = 0  # sum of all invalid IDs

    # Split the line by commas into individual ranges
    ranges = line.split(',')

    for part in ranges:
        part = part.strip()
        if not part:
            continue  # skip empty pieces (just in case)

        # Each part is like "11-22"
        start_str, end_str = part.split('-')
        start = int(start_str)
        end = int(end_str)

        # Check every number in this range
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n

    print(total)


if __name__ == "__main__":
    main()
