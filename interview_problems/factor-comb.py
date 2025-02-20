# Time Complexity  - O(n ^ 1.5)
# Space Complexity - O(log n)
def find_factors(n, factors, results, start_n):
    if n == 1:
        ordered_factors = list(sorted(factors))
        if ordered_factors not in results:
            results.append(ordered_factors)
        return results

    # In the optimal solution this is:
    # range(2, floor(sqrt(n + 1))
    for i in range(2, n+1):
        if n % i == 0 and i != start_n:
            factors.append(i)
            find_factors(n // i, factors, results, start_n)
            factors.pop()
    return results


def getFactors(n):
    return find_factors(n, [], [], n)

print(getFactors(8))
#print(getFactors(20))
