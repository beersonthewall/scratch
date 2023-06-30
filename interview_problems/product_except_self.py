from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    length = len(nums)
    result = [1] * length
    left = right = 1

    for i, n in enumerate(nums):
        result[i] *= left
        left *= n
        j = length-i-1
        result[j] *= right
        right *= nums[j]

    return result


def main():
    print(product_except_self([1,2,3,4,0]))
    print(product_except_self([1,2,3,4]))
    print(product_except_self([0,2,3,0]))

if __name__ == '__main__':
    main()
