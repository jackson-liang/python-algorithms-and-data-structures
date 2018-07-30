# This is the solution to the self-check exercise here:
# https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def rev_string(mystr):
    '''
    Input: mystr -> a string
    Output: the reversed mystr -> a string
    '''
    myStack = Stack()
    for i in range(len(mystr)):
        myStack.push(mystr[len(mystr)-1-i])
    return ''.join(myStack.items)


# Testing the function:
mystr = "abcdefghi"
print(rev_string(mystr))
