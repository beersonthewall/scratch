from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen: return True
        seen.add(n)
    return False


def main():
    print(hasDuplicate([7,1,5,3,6,4]))
    print(hasDuplicate([7,6,1,4,3,1]))
    print(hasDuplicate([]))


if __name__ == '__main__':
    main()
