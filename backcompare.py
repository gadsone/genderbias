import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from tkinter import Tk, Label, Button
import tkinter as tk

df = pd.read_csv("genderbias.csv")

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Scholarly Hazing")

        self.label = Label(master, text="What would you like to see?")
        self.label.pack()

        self.greet_button = Button(master, text="Show data", command=self.showdata)
        self.greet_button.pack()
        
        self.graph_button = Button(master, text="Show gender graph", command = self.showgraph)
        self.graph_button.pack()
        
        self.belief_button = Button(master, text="Show student beliefs", command = self.belief)
        self.belief_button.pack()
        
        self.same_button = Button(master, text="Show interaction", command = self.samegen)
        self.same_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        df = pd.read_csv("genderbias.csv")

    def showdata(self):
        window = tk.Toplevel(root)
        df.to_csv("pain.csv", encoding='utf-8', index=False)
        print(df.tail)
        
    def showgraph(self):
        
        labels = 'Male','Female','Other'
        gender_sizes = [25,40,1]
        colors=['blue','green','orange']
        explode = (0,0,0)

        plt.pie(gender_sizes, explode=explode, labels=labels, colors=colors, shadow=True, startangle=90)

        plt.title('Gender of Participants')
        plt.show()
        
    def belief(self):
        """Gender belief with options recoded to yes, no, not sure and professor recoded into yes category"""

        labels = 'Yes', 'No', 'Not sure'
        gb_sizes1 = [26,38,2]
        colors = ['yellow','red','purple']
        explode = (0,0,0)

        plt.pie(gb_sizes1, explode=explode, labels=labels, colors=colors, shadow=True, startangle=90)

        plt.title('Gender Bias Exists in USG Classrooms with Professors recoded into Yes Option')
        plt.show()
    
    def samegen(self):
        answers = ('Never', 'Rarely','Sometimes','Often','Always', 'N/A')
        responses = [4,9, 14, 27,10,2]
        y_pos = np.arange(len(answers))
        ##colors = ['blue','red','orange','green','purple','yellow']

        plt.bar(y_pos, responses, align='center',alpha=0.5, colors=colors)
        plt.xticks(y_pos,answers)
        plt.ylabel('Number of Responses')
        plt.xlabel('Options for Question')
        plt.title('Classroom Interaction with People of Same Gender')
        plt.show()

root = Tk()
root.geometry("500x200+300+300") ##width x height + position right + position down
my_gui = MyFirstGUI(root)
root.mainloop()
"""
class comparewind:
    def __init__(self, parent):
        self.parent = parent
        self.filename = "genderbias.csv"
        self.df = None
        
        self.text = tk.Text(self.parent)
        self.text.pack()
        
        self.button = tk.Button(self.parent, text = "Show Data", command = self.display)
        self.button.pack()
        
    def load(self):

        name = "genderbias.csv"

        if name:
            if name.endswith('.csv'):
                self.df = pd.read_csv(name)
            else:
                self.df = pd.read_excel(name)

            self.filename = name

            # display directly
            #self.text.insert('end', str(self.df.head()) + '\n')
    
    def display(self):
        # ask for file if not loaded yet
        if self.df is None:
            self.load()
            text = tk.Text(self)
            text.insert(tk.END, str(df.iloc[:6,1:2]))
            text.pack()

        # display if loaded
        if self.df is not None:
            self.text.insert('end', self.filename + '\n')
            self.text.insert('end', str(self.df.head()) + '\n')


# --- main ---

if __name__ == '__main__':
    root = tk.Tk()
    top = comparewind(root)
    root.mainloop()
"""

