import re
from functools import partial

def is_invalid_order(graph, order):
    return not is_valid_order(graph, order)

def is_valid_order(graph, order):
    nodes = set(order)
    seen = set()
    for node in order:
        children = filter(lambda c: c in nodes,
                          graph.get(int(node), []))
        unmet_deps = filter(lambda c: c not in seen, children)
        if any(unmet_deps):
            return False
        seen.add(node)
    return True

def parse_input(i):
    lines = i.split("\n")
    dep_pat = re.compile("[0-9]*|[0-9]*")
    deps = {}
    updates = []
    for line in lines:
        if line.find(',') > -1:
            l = line.strip()
            updates.append(list(map(lambda i: int(i), l.split(','))))
        elif dep_pat.match(line):
            match line.split("|"):
                case [a , b]:
                    d = deps.get(int(b), [])
                    d.append(int(a))
                    deps[int(b)] = d
    return deps, updates

def part_one(i):
    deps, updates = parse_input(i)
    valid_updates = list(filter(partial(is_valid_order, deps), updates))

    total = 0
    for v in valid_updates:
        middle_num = v[ (len(v) - 1) // 2 ]
        total += middle_num
    return total

from collections import Counter, deque
def top_sort(order, g):
    nodes = set(order)
    in_deg = Counter()
    for k, v in g.items():
        for child in v:
            if child in nodes and k in nodes:
                in_deg[child] += 1
    sources = deque()
    for n in nodes:
        if in_deg[n] == 0:
            sources.append(n)
    srt = []
    while sources:
        v = sources.popleft()
        srt.append(v)

        for c in g.get(v, []):
            if c in nodes:
                in_deg[c] -= 1
                if in_deg[c] == 0:
                    sources.append(c)

    if len(srt) != len(order):
        return []
    return srt

def part_two(i):
    deps, updates = parse_input(i)
    invalid_updates = list(filter(partial(is_invalid_order, deps), updates))

    total = 0
    for iv in invalid_updates:
        iv = top_sort(iv, deps)
        total += iv[ (len(iv) - 1) // 2]
    return total

if __name__ == "__main__":
    with open("input.txt") as f:
        i = f.read()
        print(part_one(i))
        print(part_two(i))

