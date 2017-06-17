class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
               " and filled: " + str(self.__filled)

class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3)/2
        return math.sqrt(s*(s-self.__side1)*(s-self.__side2)*(s-self.__side3))

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def sideCheck(self):
        if (self.__side1 + self.__side2 > self.__side3) and (self.__side1 + self.__side3 > self.__side2) and (
                        self.__side2 + self.__side3 > self.__side1):
            return True
        else:
            raise RuntimeError("Error. Cannot form a triangle.")

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)

sides = input("Enter three sides of a triangle: ")
temp = sides.split()
sideList = [eval(x) for x in temp]
triangle = Triangle(sideList[0], sideList[1], sideList[2])

if triangle.sideCheck():
    color = input("What color is the triangle? ")
    filled = eval(input("Is the triangle filled? (1 or 0) "))
    triangle.setColor(color)
    triangle.setFilled(filled)
    print(str(triangle))
    print("The area is",triangle.getArea())
    print("The perimeter is",triangle.getPerimeter())
    print("The color is",triangle.getColor())
    print("Filled: ",triangle.isFilled())
