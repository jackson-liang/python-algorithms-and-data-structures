# Exercise 2 from
# https://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/ProgrammingExercises.html
import timeit

for n in range(1000000,10000001,1000000):
    # Timing the "set item" for a dictionary
    set_timer = timeit.Timer("x[n//2] = 'another test'", "from __main__ import x,n")
    # Timing the "get item" for a dictionary
    get_timer = timeit.Timer("x[n//2]", "from __main__ import x,n")

    x = {i:'test' for i in range(n)}
    set_time = set_timer.timeit(number=1000000)
    get_time = get_timer.timeit(number=1000000)
    print("%d, %10.3f, %10.3f" % (n, set_time, get_time))
