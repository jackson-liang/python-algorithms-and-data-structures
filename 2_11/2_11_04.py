# Exercise 14from
# https://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/ProgrammingExercises.html

def get_k_th(aList, k):
    '''
    input: a list of integers in random order -> list
    input: k -> integer
    output: the k-th smallest integer in the list -> integer
    '''
    aList.sort()
    return aList[k-1]

# Testing the function
aList = [5, 6 , 3, 2, 1, 4]
print(get_k_th(aList, 5))
