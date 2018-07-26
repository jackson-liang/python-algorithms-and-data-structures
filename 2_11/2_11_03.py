# Exercise 3 from
# https://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/ProgrammingExercises.html
import timeit

for n in range(1000000,10000001,1000000):
    # Timing the del operation in lists and dictionaries
    list_del_op = timeit.Timer("del x[n//2]", "from __main__ import x,n")
    dict_del_op = timeit.Timer("del y[n//2]", "from __main__ import y,n")

    x = list(range(n))
    list_time = list_del_op.timeit(number=1)

    y = {i:None for i in range(n)}
    dict_time = dict_del_op.timeit(number=1)

    print("%d, %10.6f, %10.6f" % (n, list_time, dict_time))
