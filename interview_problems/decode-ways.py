# Decode Ways
# using the map 1 -> 'A', 2 -> 'B', etc...
#
# 11106 can be decoded as
#
# AAJF 
# KJF

from typing import Set

# Translates ints to letters per our code above
CODE_MAP = {i:chr(i+64) for i in range(1,27)}

def num_decodings(code: str) -> int:
    seen = set()
    subproblems = {}
    def decode(s: str, out: str, seen: Set) -> Set:
        nonlocal subproblems
        if not s and out not in seen:
            seen.add(out)
            return seen
        elif not s:
            return seen

        digit = int(s[0])
        if digit in CODE_MAP:
            if s[1:] in subproblems:
                seen |= subproblems[s[1:]]
            else:
                seen = decode(s[1:], out + CODE_MAP[digit], seen)
                subproblems[s[1:]] = seen

        digit = int(s[:2])
        if digit in CODE_MAP:
            if s[1:] in subproblems:
                seen |= subproblems[s[1:]]
            else:
                seen = decode(s[2:], out + CODE_MAP[digit], seen)
                subproblems[s[2:]] = seen
        return seen

    seen = decode(code, "", seen)
    return len(seen)

# Not my work
def real_solution(code: str):
    if not code or code[0] == '0':
        return 0
    n = len(code)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        od = int(code[i-1])
        td = int(code[i-2:i])
        if od != 0:
            dp[i] += dp[i-1]
        if 10 <= td <= 26:
            dp[i] += dp[i-2]
    return dp[n]

if __name__ == "__main__":
    print(num_decodings("111111111111111111111111111111111111111111111"))
    # assert num_decodings("11106") == 2
    # assert num_decodings("12") == 2
    # assert num_decodings("226") == 3
    # assert num_decodings("06") == 0

