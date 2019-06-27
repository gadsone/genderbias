##Using TKINTER 
##Source https://www.youtube.com/watch?v=RJB1Ek2Ko_Y
##Please test in PyCharm and Brackets to see if this working

from tkinter import* ##importing gui 
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from tkinter import Tk, Label, Button
import tkinter as tk


class why:
    """
    an edited version of Ebonie's original main
    
    args: none
    
    returns: none
    
    raises: none
    
    side effects: opens a window with buttons
    
    """
    def __init__(self, master):
        """
        Ebonie wrote original, Eugenia refactored
        opens a window with buttons
        args: self, master
        returns: none
        raises: none
        """
        
        url= 'https://tinyurl.com/gbusg'
        self.title = "Scholarly Hazing";
        self.master = master;
        
        self.label = Label(master, text="Scholarly Hazing");
        self.label.pack();
        
        self.button = Button(master, text="Take Survey", fg="blue", command=self.openSurvey);
        self.button.pack();
        
        self.button2 = Button(master, text="Show Data", fg="green", command=self.create_window);
        self.button2.pack();
        
        self.exitbutt = Button(master, text="Exit", fg="red", command=root.destroy);
        self.exitbutt.pack();
    
    
    url= 'https://tinyurl.com/gbusg'
    def openSurvey(self):
        """
        Ebonie wrote this
        opens survey in preferred browser
        args: self
        """
        webbrowser.open('https://tinyurl.com/gbusg')
        
    def create_window(self):
        """
        Eugenia wrote this
        creates new window/allows for "show data" to be opened in a new window
        args: self
        return: none
        raises: none
        side effects: closes original window
        """
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        bb = MyFirstGUI(self.newWindow)
        
        
df = pd.read_csv("genderbias.csv")

class MyFirstGUI:
    """
    Eugenia wrote this with the help of Ebonie
    opens window when "Show Data" is clicked
    """
    def __init__(self, master):
        """
        Eugenia wrote this
        creates the buttons in the window
        """
        self.master = master
        master.title("Scholarly Hazing")

        self.label = Label(master, text="What would you like to see?")
        self.label.pack()

        self.greet_button = Button(master, text="Export Data", command=self.showdata)
        self.greet_button.pack()
        
        self.graph_button = Button(master, text="Show Gender Graph", command = self.showgraph)
        self.graph_button.pack()
        
        self.belief_button = Button(master, text="Show Student Beliefs Graph", command = self.belief)
        self.belief_button.pack()
        
        self.same_button = Button(master, text="Show Interaction Chart", command = self.samegen)
        self.same_button.pack()

        self.close_button = Button(master, text="Close", command=self.create_window)
        self.close_button.pack()
        df = pd.read_csv("genderbias.csv")

    def showdata(self):
        """
        Eugenia wrote this
        Puts data in new CSV file
        args: self
        returns: none
        side effect: creates new CSV file and will replace 
            all of the data in that file
        """
        window = tk.Toplevel(root)
        df.to_csv("pain.csv", encoding='utf-8', index=False)
        print(df.tail)
        
    def showgraph(self):
        """
        Ebonie wrote this
        creates graph of genders in a new window
        args: self
        return: none
        raises: none
        side effects: none
        """
        
        labels = 'Male','Female','Other'
        gender_sizes = [25,40,1]
        colors=['blue','green','orange']
        explode = (0,0,0)

        plt.pie(gender_sizes, explode=explode, labels=labels, colors=colors, shadow=True, startangle=90)

        plt.title('Gender of Participants')
        plt.show()
        
    def belief(self):
        """Gender belief with options recoded to yes, no, not sure and professor recoded into yes category
        Ebonie wrote this
        args: self
        return: none
        raises: none
        side effects: none
        """

        labels = 'Yes', 'No', 'Not sure'
        gb_sizes1 = [26,38,2]
        colors = ['yellow','red','purple']
        explode = (0,0,0)

        plt.pie(gb_sizes1, explode=explode, labels=labels, colors=colors, shadow=True, startangle=90)

        plt.title('Gender Bias Exists in USG Classrooms with Professors recoded into Yes Option')
        plt.show()
    
    def samegen(self):
        """
        Ebonie wrote this
        creates graph of interaction among the same gender
        args: self
        return: none
        raises: none
        side effects: none
        """
        answers = ('Never', 'Rarely','Sometimes','Often','Always', 'N/A')
        responses = [4,9, 14, 27,10,2]
        y_pos = np.arange(len(answers))
        ##colors = ['blue','red','orange','green','purple','yellow']

        plt.bar(y_pos, responses, align='center',alpha=0.5)
        plt.xticks(y_pos,answers)
        plt.ylabel('Number of Responses')
        plt.xlabel('Options for Question')
        plt.title('Classroom Interaction with People of Same Gender')
        plt.show()
    
    def create_window(self):
        """
        Eugenia wrote this
        opens window so main can be reopened in new window
        args: self
        return: none
        raises: none
        side effects: closes original window
        """
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        bb = why(self.newWindow)

    
"""
##this was the original code that was our main window

theLabel = Label(root, text="Scholarly Hazing")
theLabel.pack()

topFrame = Frame(root)
topFrame.pack()
frame = Frame(root)
frame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

url= 'https://tinyurl.com/gbusg'


def openSurvey(url):
    webbrowser.open(url)

button1 = Button(topFrame, text= 'Take Survey',fg="blue", command=lambda aurl=url:openSurvey(aurl))
button2 = Button(topFrame, text = 'Compare Data', fg = "green")
button3 = Button(topFrame, text= 'Raw Data Graphs', fg= "orange")

exitButton = Button(root, text= 'Exit GUI', fg="red",command=root.destroy) ##this should close GUI

button1.pack()
button2.pack()
button3.pack()
exitButton.pack()
"""

if __name__ == "__main__":
    root = Tk() ##initialize 
    root.geometry("500x200+300+300") ##width x height + position right + position down
    my_gui = why(root);
    root.mainloop() ##exit program