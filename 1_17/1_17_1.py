# Exercise 1 from
# https://interactivepython.org/runestone/static/pythonds/Introduction/ProgrammingExercises.html

class Fraction:

    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

# The getNum method to return the numerator
    def getNum(self):
        return self.num

# The getDen method to return the denominator
    def getDen(self):
        return self.den

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum




# Testing the new methods
myFraction = Fraction(1,3)
print("The fraction is: "+ str(myFraction))
print("The numerator is: " + str(myFraction.getNum()))
print("The denominator is: " + str(myFraction.getDen()))
