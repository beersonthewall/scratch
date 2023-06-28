from typing import List

def productExceptSelf(nums: List[int]) -> int:
    length = len(nums)
    result = [1] * length
    left = 1
    right = 1

    for i, n in enumerate(nums):
        result[i] *= left
        left *= n
        result[length-i-1] *= right
        right *= nums[length-i-1]
    return result

def main():
    print(productExceptSelf([0,0,0]))
    print(productExceptSelf([0,3,2]))

if __name__ == '__main__':
    main()
