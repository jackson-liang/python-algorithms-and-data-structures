# Exercise 12 from
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

    def setPinA(self, x):
        self.pinA = x

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

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


def main():
    # Creating a Full Adder Circuit:
    g1 = XorGate("G1")
    g2 = AndGate("G2")
    g3 = XorGate("G3")
    g4 = AndGate("G4")
    g5 = OrGate("G5")
    c1 = Connector(g1, g3)
    sum = g3.getOutput()
    c2 = Connector(g1, g4)
    c3 = Connector(g4, g5)
    c4 = Connector(g2, g5)
    carry = g5.getOutput()
    print(sum)
    print(carry)
main()
