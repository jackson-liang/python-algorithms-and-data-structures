# Exercise 11 from
# https://interactivepython.org/runestone/static/pythonds/Introduction/ProgrammingExercises.html

class LogicGate:
    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None

    # This setPin method takes the pin value as an optional argument. If none is
    # provided it will check if it gets the value as an output from another gate,
    # and if it doesn't find one will prompt the Use for one
    def setPinA(self, a=None):
        if a==None:
            try:
                a = self.pinA.getFrom().getOutput()
            except AttributeError:
                a = int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        self.pinA = a

    def getPinA(self):
        return self.pinA

    def setPinB(self, b=None):
        if b==None:
            try:
                b = self.pinB.getFrom().getOutput()
            except AttributeError:
                b = int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        self.pinB = b

    def getPinB(self):
        return self.pinB

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0


# My XorGate which inherits from orGate
class XorGate(OrGate):
    def __init__(self,n):
        OrGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==b==0 or a==b==1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def halfAdder(x, y):
    ''' The Half Adder circuit takes 2 bits (0 or 1) as arguments and performs Gate Logic.
    '''
    g1 = XorGate("G1")
    g1.setPinA(x)
    g1.setPinB(y)
    g2 = AndGate("G2")
    g2.setPinA(x)
    g2.setPinB(y)
    sum = g1.getOutput()
    carry = g2.getOutput()
    return sum,carry

print(halfAdder(1,1))
