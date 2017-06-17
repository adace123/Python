import math

class QuadraticEquation:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getDiscriminant(self):
        return self.__b ** 2 - (4 * self.__a * self.__c)

    def getRoot1(self):
        if self.getDiscriminant() >= 0:
            return (-1 * self.__b + math.sqrt(self.getDiscriminant()))/(2 * self.__a)
        else:
            return 0

    def getRoot2(self):
        if self.getDiscriminant() >= 0:
            return (-1 * self.__b - math.sqrt(self.getDiscriminant()))/(2 * self.__a)
        else:
            return 0

a = eval(input("Enter a: "))

b = eval(input("Enter b: "))

c = eval(input("Enter c: "))

QE = QuadraticEquation(a,b,c)

if QE.getDiscriminant()> 0:
    print("Root 1:", QE.getRoot1())
    print("Root 2:", QE.getRoot2())

elif QE.getDiscriminant() == 0:
    print("The root is", QE.getRoot1())

else:
    print("The equation has no roots.")
