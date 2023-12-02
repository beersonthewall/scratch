import functools

numbers = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

def t_idx(c: str):
    return ord(c) - ord('a')
    
class TrieNode:

    def __init__(self, p):
        self.c = [None]*26
        self.p = p
        self.isEndOfWord = False

    def is_child(self, ch: str) -> bool:
        i = t_idx(ch)
        return 0 <= i < len(self.c) and self.c[t_idx(ch)] is not None

    def get_child(self, ch: str):
        return self.c[t_idx(ch)]

    def print_children(self):
        out = []
        for i, c in enumerate(self.c):
            if c:
                out.append(chr(i + 97))
        print(out)
                

class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def get_node(self, p):
        return TrieNode(p)

    def insert(self, s: str):
        s = s.lower()
        if not s:
            return

        idx = 0
        node = self.root
        while idx < len(s):
            if not s[idx].isascii():
                raise Exception("Not ascii")
            child_idx = t_idx(s[idx])
            node.c[child_idx] = node.c[child_idx] if node.c[child_idx] else self.get_node(node)
            node = node.c[child_idx]
            if idx == len(s) - 1:
                node.isEndOfWord = True

            idx += 1


    def search(self, s: str) -> bool:
        i = 0
        node = self.root
        while i < len(s):
            idx = self.index(s[i])
            if not node.c[idx]:
                return False
            node = node.c[idx]
        return node.isEndOfWord

def parse_calibration_no(s: str) -> int:
    s = s.strip()
    i = 0
    j = len(s) - 1

    while not s[i].isdigit():
        i += 1
    while not s[j].isdigit():
        j -= 1
    
    return int(s[i] + s[j])

def parse_calibration_word(t: Trie, rt: Trie, s: str) -> int:
    s = s.strip()

    i = 0
    j = len(s) - 1

    lowDigit = None
    hiDigit = None

    while i <= j and (not lowDigit or not hiDigit):
        if not lowDigit:
            if s[i].isdigit():
                lowDigit = s[i]
                continue
            idx = i
            n = t.root
            l = 0
            while n.is_child(s[idx]):
                n = n.get_child(s[idx])
                l += 1
                idx += 1
            if n.isEndOfWord:
                lowDigit = numbers[s[i:i+l]]
            i += 1

        if not hiDigit:
            if s[j].isdigit():
                hiDigit = s[j]
                continue
            idx = j
            n = rt.root
            l = 0
            while n.is_child(s[idx]):
                n = n.get_child(s[idx])
                l += 1
                idx -= 1
            if n.isEndOfWord:
                hiDigit = numbers[s[j-l+1:j+1]]
            j -= 1

    if lowDigit is None or hiDigit is None:
        raise Exception("not found")

    res = int(lowDigit + hiDigit)
    return res



def main():
    with open('inputs/day1.txt') as f:
        data = f.readlines()
        p1 = sum(map(parse_calibration_no, data))
        t = Trie()
        rt = Trie()
        for n in numbers.keys():
            t.insert(n)
            rt.insert(n[::-1])

        p2 = sum(map(functools.partial(parse_calibration_word, t, rt), data))
        print(f"part 1: {p1}")
        print(f"part 2: {p2}")

if __name__ == '__main__':
    main()
