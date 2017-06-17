import math
import os.path
import sys

def computeScores():
    filename = input("Enter a Python source code filename: ").strip()
    scoreCount = 0
    sum = 0
    if not os.path.isfile(filename):
        print("File", filename, "does not exist")
        sys.exit()

    infile = open(filename, "r")

    scores = infile.read().split()

    scoresList = [eval(x) for x in scores]

    for i in range(len(scoresList)):
        scoreCount+=1
        sum+=scoresList[i]

    print("There are",scoreCount,"scores")
    print("The total is",sum)
    print("The average is",sum/scoreCount)

computeScores()
