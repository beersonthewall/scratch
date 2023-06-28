from typing import List

def twoSum(arr: List[int], target: int) -> List[int]:
    diffs = {}
    for i, n in enumerate(arr):
        diff = target - n
        if diff in diffs:
            return [i, diffs[diff]]
        else:
            diffs[n] = i
    return []

def main():
    print(twoSum([2,7,11,15], 9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3], 6))


if __name__ == '__main__':
    main()
