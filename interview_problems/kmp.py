from typing import List

def generate_prefixes(pat: str) -> List[int]:
    p = [0] * (len(pat) + 1)
    p[0] = -1
    p[1] = 0

    i = 1
    prefixLen = 0

    while i < len(pat):
        if pat[i] == pat[prefixLen]:
            i += 1
            prefixLen += 1
            p[i] = prefixLen
        elif prefixLen > 0:
            prefixLen = p[prefixLen]
        else:
            i += 1
            p[i] = 0
    return p


def kmp(s: str, pat: str) -> List[int]:
    prefixLengths = generate_prefixes(pat)
    s_pos = pat_pos = 0
    matches = []
    while s_pos < len(s):
        if pat[pat_pos] == s[s_pos]:
            s_pos += 1
            pat_pos += 1
            if pat_pos == len(pat):
                matches.append(s_pos - pat_pos)
                pat_pos = prefixLengths[pat_pos]
        else:
            pat_pos = prefixLengths[pat_pos]
            if pat_pos < 0:
                s_pos += 1
                pat_pos += 1

    return matches

if __name__ == '__main__':
    print(generate_prefixes("abcxxxabcy"))
    print(kmp("---abcxxxab------abcxxxabcy---", "abcxxxabcy"))
