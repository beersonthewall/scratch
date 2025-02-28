from collections import Counter

def get_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        return lines

def part_one():
    lhs = []
    rhs = []
    for l in get_lines():
        items = l.split('   ')
        lhs.append(items[0])
        rhs.append(items[1])

    lhs = list(sorted(lhs))
    rhs = list(sorted(rhs))

    td = 0
    for (x, y) in zip(lhs, rhs):
        td += abs(int(x) - int(y))
    return td

def part_two():
    lhs = []
    rhs = Counter()
    for l in get_lines():
        items = l.split('   ')
        lhs.append(int(items[0]))
        rhs[int(items[1])] += 1

    score = 0
    for num in lhs:
        if num in rhs:
            score += num * rhs[num]
    return score

def main():
    print(part_one())
    print(part_two())

if __name__ == '__main__':
    main()
