# Exercise 3 from
# https://interactivepython.org/runestone/static/pythonds/Introduction/ProgrammingExercises.html

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:
    # The fraction is maintained in lowest terms in initalization
    def __init__(self,top,bottom):
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    # The getNum method to return the numerator
    def getNum(self):
        return self.num

    # The getDen method to return the denominator
    def getDen(self):
        return self.den

    # Modifed the add method, which doesnt need to reduce anymore
    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    # The subtract method
    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    # The multiplication method
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    # The true division method
    def __truediv__(self, other):
        return self.num*other.den / self.den*other.num

# Testing the new methods
myFraction1 = Fraction(2,12)
myFraction2 = Fraction(6,24)
print(myFraction1 - myFraction2)
print(myFraction1 * myFraction2)
print(myFraction1 / myFraction2)
