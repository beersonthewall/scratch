import cProfile
from typing import List

"""
$ python list-comprehension-benchmark.py 
         2706 function calls (1807 primitive calls) in 0.053 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.053    0.053 <string>:1(<module>)
        1    0.000    0.000    0.053    0.053 list-comprehension-benchmark.py:41(a)
    900/1    0.003    0.000    0.053    0.053 list-comprehension-benchmark.py:42(recursive_helper)
      899    0.049    0.000    0.049    0.000 list-comprehension-benchmark.py:47(<listcomp>)
        1    0.000    0.000    0.000    0.000 typing.py:255(inner)
        1    0.000    0.000    0.000    0.000 typing.py:720(__hash__)
        1    0.000    0.000    0.053    0.053 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
      900    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1807 function calls (908 primitive calls) in 0.052 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.052    0.052 <string>:1(<module>)
        1    0.000    0.000    0.052    0.052 list-comprehension-benchmark.py:56(b)
    900/1    0.052    0.000    0.052    0.052 list-comprehension-benchmark.py:57(recursive_helper)
        1    0.000    0.000    0.000    0.000 typing.py:255(inner)
        1    0.000    0.000    0.000    0.000 typing.py:720(__hash__)
        1    0.000    0.000    0.052    0.052 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
      900    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         406357 function calls (405458 primitive calls) in 0.099 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.099    0.099 <string>:1(<module>)
        1    0.000    0.000    0.099    0.099 list-comprehension-benchmark.py:70(c)
    900/1    0.080    0.000    0.099    0.099 list-comprehension-benchmark.py:71(recursive_helper)
        1    0.000    0.000    0.000    0.000 typing.py:255(inner)
        1    0.000    0.000    0.000    0.000 typing.py:720(__hash__)
        1    0.000    0.000    0.099    0.099 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
      900    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   404550    0.019    0.000    0.019    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

def a(nums: List[int]) -> int:
    def recursive_helper(array: List[int]):
        N = len(array)
        if N == 1:
            return array

        newNums = [
            (array[i] + array[i+1]) % 10
            for i in range(N - 1)
        ]

        return recursive_helper(newNums)

    return recursive_helper(nums)[0]

def b(nums: List[int]):
    def recursive_helper(array: List[int]):
        N = len(array)
        if N == 1:
            return array

        newNums = [0] * (N - 1)
        for i in range(N - 1):
            newNums[i] = (array[i] + array[i+1]) % 10

        return recursive_helper(newNums)

    return recursive_helper(nums)[0]

def c(nums: List[int]):
    def recursive_helper(array: List[int]):
        N = len(array)
        if N == 1:
            return array

        newNums = []
        for i in range(N - 1):
            newNums.append((array[i] + array[i+1]) % 10)

        return recursive_helper(newNums)

    return recursive_helper(nums)[0]

if __name__ == '__main__':
    inputs = [
        [x for x in range(900)],
    ]

    for i in inputs:
        cProfile.run("a(i)")
        cProfile.run("b(i)")
        cProfile.run("c(i)")
