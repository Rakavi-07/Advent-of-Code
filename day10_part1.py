import sys
import re

def parse_line(line):
    diagram = re.search(r"\[([.#]+)\]", line).group(1)
    target = [1 if c == "#" else 0 for c in diagram]
    n = len(target)

    buttons = []
    for grp in re.findall(r"\((.*?)\)", line):
        if grp.strip() == "":
            buttons.append([])
        else:
            buttons.append(list(map(int, grp.split(","))))

    return n, target, buttons


def min_presses(n, target, buttons):
    m = len(buttons)
    best = 10**9

    for mask in range(1 << m):
        lights = [0] * n
        presses = 0

        for i in range(m):
            if (mask >> i) & 1:
                presses += 1
                for idx in buttons[i]:
                    lights[idx] ^= 1

        if lights == target:
            best = min(best, presses)

    return best


def main():
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n, target, buttons = parse_line(line)
        total += min_presses(n, target, buttons)

    print(total)


if __name__ == "__main__":
    main()
