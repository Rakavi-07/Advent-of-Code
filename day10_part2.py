import sys
import re
from heapq import heappush, heappop

line_re = re.compile(r"\[(.*?)\]\s+(.*)\s+\{(.*?)\}")

def parse_line(line):
    m = line_re.match(line)
    if not m:
        return None

    buttons_part = m.group(2)
    target = list(map(int, m.group(3).split(",")))

    buttons = []
    for b in re.findall(r"\((.*?)\)", buttons_part):
        if b.strip() == "":
            buttons.append([])
        else:
            buttons.append(list(map(int, b.split(","))))

    return target, buttons


def min_presses(target, buttons):
    n = len(target)
    start = tuple([0] * n)
    goal = tuple(target)

    pq = [(0, start)]
    seen = set([start])

    while pq:
        cost, state = heappop(pq)
        if state == goal:
            return cost

        for btn in buttons:
            nxt = list(state)
            ok = True
            for i in btn:
                nxt[i] += 1
                if nxt[i] > target[i]:
                    ok = False
                    break
            if not ok:
                continue

            nxt = tuple(nxt)
            if nxt not in seen:
                seen.add(nxt)
                heappush(pq, (cost + 1, nxt))

    return float("inf")


def main():
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parsed = parse_line(line)
        if not parsed:
            continue

        target, buttons = parsed
        total += min_presses(target, buttons)

    print(total)


if __name__ == "__main__":
    main()
