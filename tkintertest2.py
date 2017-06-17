class Shapes:
    def __init__(self):
        window = Tk()
        window.title("Shapes")
        self.fillCheck=1
        self.canvas = Canvas(window,width=400,height=200,bg="white")
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        self.s = StringVar()
        self.f = IntVar()
        Radiobutton(frame, text="Rectangle", command=self.processRadiobutton, variable=self.s, value="R").grid(row=2,column=1)
        Radiobutton(frame, text="Oval", command=self.processRadiobutton,variable=self.s,value="O").grid(row=2,column=2)
        Checkbutton(frame,text="Fill",variable=self.f,command=self.fillCanvas).grid(row=2,column=3)
        window.mainloop()

    def processRadiobutton(self):
        if self.s.get() == "R":
            self.displayRect()
        elif self.s.get() == "O":
            self.displayOval()

    def displayRect(self):
        self.clearCanvas()

        self.canvas.create_rectangle(25, 10, 380, 120, tags="rect")


    def displayOval(self):
        self.clearCanvas()

        self.canvas.create_oval(10, 10, 380, 120, tags="oval")




    def clearCanvas(self):
        self.canvas.delete("rect", "oval")

    def fillCanvas(self):
        self.fillCheck+=1

        if self.fillCheck % 2 !=0 and self.s.get()=="O":
            self.displayOval()
        elif self.fillCheck % 2 ==0 and self.s.get()=="O":
            self.clearCanvas()
            self.canvas.create_oval(25, 10, 380, 120, fill="black", tags="oval")

        elif self.fillCheck % 2 !=0 and self.s.get()=="R":
            self.displayRect()
        elif self.fillCheck % 2 ==0 and self.s.get()=="R":
            self.clearCanvas()
            self.canvas.create_rectangle(25, 10, 380, 120, fill="black", tags="rect")


Shapes()
