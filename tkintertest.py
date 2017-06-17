from tkinter import *

class Car:
    def __init__(self):
        window = Tk()
        window.title("Race Car")
        self.canvas = Canvas(window, width=400, height=200, bg="white")
        self.canvas.pack()
        self.radiusX = 0
        self.radiusY = 200
        self.tire1 = self.canvas.create_oval(self.radiusX+30,self.radiusY-25,self.radiusX+55,self.radiusY,fill="black",tags="tire1")
        self.tire2 = self.canvas.create_oval(self.radiusX + 100, self.radiusY - 25, self.radiusX + 75, self.radiusY,fill="black",tags="tire2")
        self.body = self.canvas.create_rectangle(10,175,120,150,fill="blue",tags="body")
        self.top = self.canvas.create_polygon(25,150,55,125,75,125,105,150,fill="purple",tags="top")
        x=0
        width = 400
        self.dx=4
        self.sleepTime = 15
        self.canvas.bind("<Up>",self.speedUp)
        self.canvas.bind("<Down>",self.slowDown)
        self.canvas.focus_set()
        while True:
            self.canvas.move("tire1",self.dx,0)
            self.canvas.move("tire2", self.dx, 0)
            self.canvas.move("body", self.dx, 0)
            self.canvas.move("top", self.dx, 0)
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            if x<width:
                x+=self.dx
            else:
                x=0
                self.canvas.delete("tire1")
                self.canvas.delete("tire2")
                self.canvas.delete("body")
                self.canvas.delete("top")
                self.tire1 = self.canvas.create_oval(self.radiusX + 30, self.radiusY - 25, self.radiusX + 55,
                                                     self.radiusY, fill="black", tags="tire1")
                self.tire2 = self.canvas.create_oval(self.radiusX + 100, self.radiusY - 25, self.radiusX + 75,
                                                     self.radiusY, fill="black", tags="tire2")
                self.body = self.canvas.create_rectangle(10, 175, 120, 150, fill="blue", tags="body")
                self.top = self.canvas.create_polygon(25, 150, 55, 125, 75, 125, 105, 150, fill="purple", tags="top")
        window.mainloop()

    def speedUp(self,event):
        self.dx+=3

    def slowDown(self,event):
        if self.dx>3:
            self.dx-=3
        elif self.dx<3 and self.dx>0:
            self.dx=0
        else:
            self.dx=4

Car()
