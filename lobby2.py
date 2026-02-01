import sys

def max_joltage_for_bank(line: str, k: int = 12) -> int:
    """
    Given a string of digits (one bank), find the maximum k-digit number
    you can form by choosing k digits in order (subsequence).
    """
    digits = line.strip()
    n = len(digits)
    to_remove = n - k  # how many digits we're allowed to drop

    stack = []

    for ch in digits:
        # While we can still remove digits and the last chosen digit is smaller
        # than the current one, pop it to make the number bigger.
        while to_remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1

        stack.append(ch)

    # If we didn't remove enough, just cut from the end
    result_digits = ''.join(stack[:k])
    return int(result_digits)


def main():
    total = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue  # skip empty lines

        bank_max = max_joltage_for_bank(line, k=12)
        total += bank_max

    print(total)


if __name__ == "__main__":
    main()
