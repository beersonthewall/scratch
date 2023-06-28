def solve_knapsack(profits, weights, capacity):
  return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_bot_up_min_space(profits, weights, capacity):
    numItems = len(profits)
    if capacity <= 0 or numItems == 0 or len(weights) != numItems:
        return 0

    # Space optimization: can use i % 2 for all lookups because
    # we only need memo[_][i] and memo[_][i-1].
    memo = [[0 for _ in range(2)] for _ in range(capacity+1)]

    # Solutions for capacity = 0 are always 0
    for i in range(2):
        memo[0][i] = 0

    # Solutions for first item at every possible capacity
    for c in range(capacity+1):
        if weights[0] <= c:
            memo[c][0] = profits[0]

    for c in range(1, capacity + 1):
        for index in range(1, numItems):
            pickProfit, passProfit = 0, memo[c][(index-1)%2]
            if weights[index] <= c:
                pickProfit += profits[index] + memo[c-weights[index]][(index-1) % 2]
            memo[c][index % 2] = max(passProfit, pickProfit)

    return memo[capacity][(numItems-1)%2]


def knapsack_bot_up(profits, weights, capacity):
    numItems = len(profits)
    if capacity <= 0 or numItems == 0 or len(weights) != numItems:
        return 0

    memo = [
        [0 for _ in range(len(profits))] for _ in range (capacity + 1)
    ]

    # Solutions for capacity = 0 are always 0
    for i in range(numItems):
        memo[0][i] = 0

    # Solutions for first item at every possible capacity
    for c in range(capacity+1):
        if weights[0] <= c:
            memo[c][0] = profits[0]

    for c in range(1, capacity + 1):
        for index in range(1, numItems):
            pickProfit, passProfit = 0, memo[c][index-1]
            if weights[index] <= c:
                pickProfit += profits[index] + memo[c-weights[index]][index-1]
            memo[c][index] = max(passProfit, pickProfit)

    return memo[capacity][numItems-1]
    

def memoized_knapsack(profits, weights, capacity):
    """
    Top-down memoization solution for 0/1 knapsack problem.
    """
    # memo[capacity][currentIndex]
    memo = [[-1 for _ in range(len(profits))] for _ in range(capacity + 1)]

    def recursive(profits, weights, capacity, currentIndex):
        nonlocal memo

        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        if memo[capacity][currentIndex] != -1:
            return memo[capacity][currentIndex]

        pickProfit = 0
        if weights[currentIndex] <= capacity:
            pickProfit += profits[currentIndex]
            pickProfit += recursive(profits,
                                    weights,
                                    capacity - weights[currentIndex],
                                    currentIndex + 1)
        leaveProfit = recursive(profits,
                                weights,
                                capacity,
                                currentIndex + 1)
        localSolution = max(pickProfit, leaveProfit)
        memo[capacity][currentIndex] = localSolution
        return localSolution

    return recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, currentIndex):
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    pickProfit = 0
    if weights[currentIndex] <= capacity:
        pickProfit = profits[currentIndex] + knapsack_recursive(profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    nopick = knapsack_recursive(profits, weights, capacity, currentIndex + 1)

    return max(pickProfit, nopick)

def main():
    print(solve_knapsack([1,6,10,16], [1,2,3,5], 7))
    print(knapsack_bot_up([1,6,10,16], [1,2,3,5], 7))
    print(knapsack_bot_up_min_space([1,6,10,16], [1,2,3,5], 7))
    
if __name__ == '__main__':
    main()

