def p1():
    with open('inputs/day3.txt') as f:
        data = f.read().strip()
        lines = data.split('\n')
        total = 0
        start = end = 0
        isSymbolAdj = False
        for row, line in enumerate(lines):
            if start != end and isSymbolAdj:
                number = int(lines[row-1][start:end])
                total += number

            start = end = 0
            isSymbolAdj = False

            for col, c in enumerate(line):
                if c.isdigit():
                    end += 1
                    for x,y in [(-1,0), (0,-1), (1,0), (0,1), (1,1), (1,-1), (-1,-1), (-1,1)]:
                        dx = row + x
                        dy = col + y
                        if 0 <= dx < len(lines) and \
                           0 <= dy < len(line) and \
                           (not lines[dx][dy].isdigit() and lines[dx][dy] != '.'):
                            isSymbolAdj = True
                else:
                    if start != end and isSymbolAdj:
                        number = int(line[start:end])
                        total += number
                    start = end = col + 1
                    isSymbolAdj = False
        print(total)

def find_ratio(M, x, y) -> int:
    seen = {(x,y)}
    DIRS = [(-1,0), (0,-1), (1,0), (0,1), (1,1), (1,-1), (-1,-1), (-1,1)]

    stack = []
    for a, b in DIRS:
        dx = x + a
        dy = y + b
        if 0 <= dx < len(M) and \
           0 <= dy < len(M[dx]) and \
           M[dx][dy].isdigit():
            stack.append((dx,dy))

    numbers = []
    while stack:
        (a, b) = stack.pop()
        if (a, b) in seen:
            continue
        start = end = b
        while start >= 0 and M[a][start].isdigit():
            start -= 1
            seen.add((a, start))
        while end < len(M[a]) and M[a][end].isdigit():
            end += 1
            seen.add((a, end))
        numbers.append(int(M[a][start+1:end]))
    print(numbers)
    return numbers[0] * numbers[1] if len(numbers) == 2 else 0

def p2():
    GEAR = '*'
    with open('inputs/day3.txt') as f:
        data = f.read().strip()
        lines = data.split('\n')

        ratio_sum = 0
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                item = lines[row][col]
                if item == GEAR:
                    ratio_sum += find_ratio(lines, row, col)
        print(ratio_sum)
            

def main():
    p1()
    p2()

if __name__ == '__main__':
    main()

