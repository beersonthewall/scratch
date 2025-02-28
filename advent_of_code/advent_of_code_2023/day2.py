from typing import Optional

MAXIMUMS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def check(line: str) -> Optional[int]:
    colon_idx = line.find(':')
    game_id = int(line[5:colon_idx])

    subsets = line[colon_idx+1:].split(';')
    for s in subsets:
        colors = s.split(',')
        for c in colors:
            c = c.strip()
            i = 0
            while i < len(c) and c[i].isdigit():
                i += 1
            amount = int(c[0:i+1])
            if c.find('red') > 0 and amount > MAXIMUMS['red']:
                return None
            elif c.find('green') > 0 and amount > MAXIMUMS['green']:
                return None
            elif c.find('blue') > 0 and amount > MAXIMUMS['blue']:
                return None

    return game_id

def p2(line):
    colon_idx = line.find(':')
    game_id = int(line[5:colon_idx])

    subsets = line[colon_idx+1:].split(';')

    max_red = 0
    max_green = 0
    max_blue = 0

    for s in subsets:
        colors = s.split(',')
        for c in colors:
            c = c.strip()
            i = 0
            while i < len(c) and c[i].isdigit():
                i += 1
            amount = int(c[0:i+1])
            if c.find('red') > 0 and amount > max_red:
                max_red = amount
            elif c.find('green') > 0 and amount > max_green:
                max_green = amount
            elif c.find('blue') > 0 and amount > max_blue:
                max_blue = amount

    return max_red * max_blue * max_green
    

def main():
    with open('inputs/day2.txt') as f:
        lines = f.readlines()
        print(sum(filter(None, map(check, lines))))
        print(sum(filter(None, map(p2, lines))))
        

if __name__ == '__main__':
    main()


