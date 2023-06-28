from typing import List
import math

def maxProfit(prices: List[int]) -> int:
    smallest = math.inf
    mp = 0
    for p in prices:
        smallest = min(p, smallest)
        mp = max(mp, p-smallest)
    return mp

def main():
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))


if __name__ == '__main__':
    main()
