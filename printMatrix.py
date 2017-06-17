import random

def printMatrix(n):
    count=0
    for i in range(n):
        for j in range(n):
            count+=1
            randNum = random.randint(0, 1)
            print(randNum, end=" ")
            if count%n==0:
                print()


num = eval(input("Enter n: "))

printMatrix(num)
