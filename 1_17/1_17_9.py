# Exercise 9 from
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
        # Checking if both num and den are ints
        if not(type(top)==int and type(bottom)==int):
            raise TypeError("The Numerator and Denominator should both be integers!")
        else:
            # Checking if the denominator is a negative number
            if bottom < 0:
                bottom = -bottom
                top = -top
            common = gcd(top, bottom)
            self.num = top // common
            self.den = bottom // common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    # Defined the __repr__ method which returns a representation of the Fraction
    # which can be evaluated
    def __repr__(self):
        return "Fraction(" + str(self.num) + "," + str(self.den) + ")"

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

    # Defining the __radd__ method, and since adding 2 fractions is commutative, then
    # __radd__ is the same as __add__
    def __radd__(self, other):
        return self.__add__(other)

    # Defining the __iadd__ method.
    def __iadd__(self, other):
        newFrac = self.__add__(other)
        self.num = newFrac.getNum()
        self.den = newFrac.getDen()

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

    # The "greater than" method
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    # The "greater or equal than" method
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    # The "less than" method
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    # The "greater than" method
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    # The "not equal" method
    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum

# Testing the new methods
myFraction = Fraction(2,12)
otherFraction = Fraction(2,4)
print(str(myFraction))
print(repr(myFraction))
print(eval(repr(myFraction)))
