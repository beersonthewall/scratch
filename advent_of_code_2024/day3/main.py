import re

def part_one(input):
    pat = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    m = pat.findall(input)
    total = 0
    for match in m:
        x = int(match[0])
        y = int(match[1])
        total += x * y
    return total

def part_two(input):
    pat = re.compile("(do\(\))|(don't\(\))|mul\(([0-9]+),([0-9]+)\)")
    total = 0

    last_op = ""
    for match in pat.findall(input):
        if match[0]:
            last_op = match[0]
        elif match[1]:
            last_op = match[1]

        if last_op != "don't()" and match[2] and match[3]:
            x = int(match[2])
            y = int(match[3])
            total += x * y
            last_op = ""
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()
        print(part_one(input))
        print(part_two(input))

