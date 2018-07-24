# This is the solution to the self-check exercise here:
# https://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/BigONotation.html

# The first function which finds the minimum number in a list is O(n2)
def min_list_1(list):
    '''
    Input: a list of integers
    Output: an integer
    '''
    for l in list:
        for i in list:
            if l > i:
                break
            else:
                minimum = l
    return minimum

# The second function which finds the minimum number in a list is O(n)
def min_list_2(list):
    '''
    Input: a list of integers
    Output: an integer
    '''
    minimum = list[0]
    for l in list:
        if l < minimum:
            minimum = l
    return minimum

print(min_list_1([3,1,2,0,5,-1,8,6,-1]))
print(min_list_2([3,1,2,0,5,-1,8,6,-1]))
