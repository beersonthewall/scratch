def max_unique_substrings(s):
    result = []
    for i in range(len(s)):
        letter = s[i]
        if letter not in result:
            result.append(letter)
        else:
            result[-1] + letter;

    return len(result)

print(max_unique_substrings("aab"))
print(max_unique_substrings("abcabc"))

