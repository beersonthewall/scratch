"""
Given an array of positive integers `numbers` and a positive number `separation`.
Find the minimal difference between elements of `numbers` with indicies that
are at least `separatation` apart. Formally find:
`min(|numbers[i] - numbers[j]|) where |i-j| >= separation`

2 <= numbers.length <= 10^5
1 <= numbers[i] <= 10^9
"""

from typing import List
from math import inf as Infinity

def minSeparation(nums: List[int], sep: int) -> int:
    """
    Solution ideas:

    Sliding window
    """
    smallest = Infinity
    for i in range(len(nums)):
        end = i + sep
        while end < len(nums):
            smallest = min(smallest, abs(nums[end] - nums[i]))
            end += 1
    return smallest

def find(nums, n):
    low = 0
    high = len(nums) - 1
    while low < high:
        mp = low + ((high - low) // 2)
        if n == nums[mp]:
            return n
        elif n < nums[mp]:
            high = mp - 1
        else:
            low = mp + 1
    return nums[low]

def minSepBinarySearch(nums: List[int], sep: int) -> int:
    sortedNums = list(sorted(nums[sep:]))
    smol = Infinity
    for i in range(len(nums)-sep):
        closest = find(sortedNums, nums[i])
        smol = min(smol, abs(nums[i] - closest))
        sortedNums.remove(nums[i+sep])
    return smol
   
def main():
    assert(minSeparation([1,5,4,10,9], 3) == 4)
    assert(minSeparation([3,10,5,8], 1) == 2)
    assert(minSepBinarySearch([1,5,4,10,9], 3) == 4)
    assert(minSepBinarySearch([3,10,5,8], 1) == 2)
    print("All cases passed")


if __name__ == '__main__':
    main()

