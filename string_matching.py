def matches(pat: str, s: str) -> bool:
    optionals = set()
    reducedPat = ""
    prev = ''

    for c in pat:
        if c == '?':
            optionals.add(prev)
        else:
            prev = c
            reducedPat += c

    patternIndex = 0

    for textChar in s:

        if patternIndex >= len(reducedPat):
            return False

        patChar = reducedPat[patternIndex]
        if textChar == patChar:
            patternIndex += 1
        elif textChar != patChar and patChar in optionals:
            #patternIndex += 1
            while patternIndex < len(reducedPat):
                patternIndex += 1
                if patChar == textChar:
                    patternIndex += 1
                    break
                elif patChar in optionals:
                    patternIndex += 1
        else:
            return False

    for patChar in reducedPat[patternIndex:]:
        if patChar in optionals:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    cases = [
        ("abc", "abc", True),
        ("abc", "bc", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("a?", "", True),
        ("a?", "a", True),
        ("a?", "ab", False),
        ("a?", "b", True),
        ("a?bc?d", "abd", True),
        ("a?bc?d", "acd", False),
        ("a?bc?d", "bbd", False),
        ("aa?a", "aa", True),
        ("aa?a", "aaa", True),
        ("aa?a", "aaab", False),
        ("ab", "abc", False),
        ("abc", "", False),
        ("abc", "a", False),
        ("abc", "abc", True),
        ("abc", "bc", False),
        ("def", "de", False)
    ]


    failures = []
    for (s, pat, result) in cases:
        if matches(s, pat) != result:
            failures.append((s, pat, result))

    if failures:
        print("Some test cases failed:")
        for f in failures:
            print(f)
    else:
        print("All cases passed :)")
    
