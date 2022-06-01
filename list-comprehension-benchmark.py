import cProfile
from typing import List

"""
$ python list-comprehension-benchmark.py 
         2706 function calls (1807 primitive calls) in 0.049 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.049    0.049 <string>:1(<module>)
      899    0.046    0.000    0.046    0.000 list-comprehension-benchmark.py:11(<listcomp>)
        1    0.000    0.000    0.049    0.049 list-comprehension-benchmark.py:5(a)
    900/1    0.003    0.000    0.049    0.049 list-comprehension-benchmark.py:6(recursive_helper)
        1    0.000    0.000    0.000    0.000 typing.py:255(inner)
        1    0.000    0.000    0.000    0.000 typing.py:720(__hash__)
        1    0.000    0.000    0.049    0.049 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
      900    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         406357 function calls (405458 primitive calls) in 0.102 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.102    0.102 <string>:1(<module>)
        1    0.000    0.000    0.102    0.102 list-comprehension-benchmark.py:21(b)
    900/1    0.081    0.000    0.102    0.102 list-comprehension-benchmark.py:22(recursive_helper)
        1    0.000    0.000    0.000    0.000 typing.py:255(inner)
        1    0.000    0.000    0.000    0.000 typing.py:720(__hash__)
        1    0.000    0.000    0.102    0.102 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
      900    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   404550    0.020    0.000    0.020    0.000 {method 'append' of 'list' objects}
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

    x = recursive_helper(nums)
    return x[0]

def b(nums: List[int]):
    def recursive_helper(array: List[int]):
        N = len(array)
        if N == 1:
            return array

        newNums = []
        for i in range(N - 1):
            newNums.append((array[i] + array[i+1]) % 10)

        return recursive_helper(newNums)

    x = recursive_helper(nums)
    return x[0]

if __name__ == '__main__':
    inputs = [
        [x for x in range(900)],
    ]

    for i in inputs:
        cProfile.run("a(i)")
        cProfile.run("b(i)")
