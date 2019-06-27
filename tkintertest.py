from tkinter import *
class Class1:
    def __init__(self):
        self.root=Tk()
        self.root.title("test")
        self.root.resizable(width=False, height=False)
        self.can1=Canvas(self.root, width=500, height=500, bg="black")
        self.can1.pack(expand=False, fill=X)
        obj2 = Class2()
        b1 = Button(self.can1,text="button 1",command=obj2.button1)
        self.can1.create_window(20,20, window=b1, anchor = NW)
class Class2:
    def __init__(self):
        pass
    def button1(self):
        self.window2=Toplevel(bg = 'black')
        self.window2.title("test window 2")
        self.window2.resizable(width=False, height=False)
        self.window2.grid()
        self.can2=Canvas(self.window2, width=500, height=500, bg="black")
gui = Class1()
gui.root.mainloop()