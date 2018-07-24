# Exercise 1 from
# https://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/ProgrammingExercises.html
import timeit

# We are timing the index operator in a Python list.
index_op = timeit.Timer("x[n//2]", "from __main__ import x,n")

# For different n's the time should remain the same (almost).
for n in range(1000000,10000001,1000000):
    x = list(range(n))
    print(index_op.timeit(number=1000000))
