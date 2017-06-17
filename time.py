import time

class Time:
    def __init__(self):
        self.__hour = int(((time.time() // 60) // 60) % 24)
        self.__minute = int((time.time() // 60) % 60)
        self.__second = int(time.time() % 60)

    def getHour(self):
        return str(format(self.__hour,"2d"))

    def getMinute(self):
        return str(format(self.__minute,"2d"))

    def getSecond(self):
        return str(format(self.__second,"2d"))

    def setTime(self, elapseTime):
        self.__hour = ((elapseTime // 60) // 60) % 24
        self.__minute = (elapseTime // 60) % 60
        self.__second = elapseTime % 60

t = Time()

print("Current time is",t.getHour() + ":" + t.getMinute() + ":" +t.getSecond())

userTime = eval(input("Enter the elapsed time: "))

t.setTime(userTime)
print("The hour:minute:second for the elapsed time is",t.getHour() + ":" + t.getMinute() + ":" +t.getSecond())
