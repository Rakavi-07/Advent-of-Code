import sys

def max_two_digit_for_bank(line: str) -> int:
    """
    Given a string of digits (one bank), find the maximum
    2-digit number you can form by choosing two digits
    in order (i < j).
    """
    digits = [int(ch) for ch in line.strip()]
    n = len(digits)

    max_val = -1  # will store maximum 2-digit value

    # Try all pairs (i, j) with i < j
    for i in range(n):
        for j in range(i + 1, n):
            val = 10 * digits[i] + digits[j]
            if val > max_val:
                max_val = val

    return max_val


def main():
    total = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue  # skip empty lines

        bank_max = max_two_digit_for_bank(line)
        total += bank_max

    print(total)


if __name__ == "__main__":
    main()
