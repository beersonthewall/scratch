import re

def match_pats(pats, input):
    total = 0
    for pat in pats:
        p = re.compile(pat)
        total += len(p.findall(input))
    return total
    
def part_one(input):
    w = input.find("\n")
    input = input.replace("\n", " ")

    pats = [
        "XMAS",
        f"(?=X.{{{w}}}M.{{{w}}}A.{{{w}}}S)",
        f"(?=X.{{{w + 1}}}M.{{{w + 1}}}A.{{{w + 1}}}S)",
        f"(?=X.{{{w - 1}}}M.{{{w - 1}}}A.{{{w - 1}}}S)",
        "(?=SAMX)",
        f"(?=S.{{{w}}}A.{{{w}}}M.{{{w}}}X)",
        f"(?=S.{{{w + 1}}}A.{{{w + 1}}}M.{{{w + 1}}}X)",
        f"(?=S.{{{w - 1}}}A.{{{w - 1}}}M.{{{w - 1}}}X)",
    ]

    return match_pats(pats, input)

def part_two(input):
    w = input.find("\n")
    input = input.replace("\n", " ")
    pats = [
        f"(?=M.S.{{{w-1}}}A.{{{w-1}}}M.S)",
        f"(?=S.S.{{{w-1}}}A.{{{w-1}}}M.M)",
        f"(?=M.M.{{{w-1}}}A.{{{w-1}}}S.S)",
        f"(?=S.M.{{{w-1}}}A.{{{w-1}}}S.M)",
    ]
    return match_pats(pats, input)

if __name__ == "__main__":
    with open("input.txt") as f:
        i = f.read()
        print(part_one(i))
        print(part_two(i))

