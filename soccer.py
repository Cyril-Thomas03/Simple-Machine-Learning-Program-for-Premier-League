
# importing all necessary modules to run program
import tkinter
import tkinter.messagebox
from tkinter import *
from sklearn import svm
import pandas as pd
import numpy as np


# function used to run data into machine learning
def calculate():
   # Importing the data
   data = pd.read_csv("soccer.csv", sep=",")

   # taking desired attributes from data
   data = data[["goals_overall", "assists_overall", "yellow_cards_overall", "min_per_match", "appearances_overall", "age",
                "red_cards_overall"]]

   # label that will be predicted
   predict = "min_per_match"

   # returns a new data frame without G3
   x = np.array(data.drop([predict], 1))
   # returns data frame with only G3
   y = np.array(data[predict])

   # assigning variables
   x_train = x
   y_train = y

   # Implementing the classifier for machine learning
   clf = svm.SVC(kernel="linear", C=2)
   clf.fit(x_train, y_train)

   # Changing inputted data into preferable forms
   data_1 = int(goals_overall.get())
   data_2 = int(assists_overall.get())
   data_3 = int(yellow_cards.get())
   data_4 = int(red_cards.get())
   data_5 = int(appearances.get())
   data_6 = int(age.get())

   # Assigning variables as inputted data
   new_data = np.array([[data_1, data_2, data_3, data_4, data_5, data_6]])

   # Predicting final mark based on model built
   predictions = clf.predict(new_data)

   # Displaying final mark on label
   final_mark = tkinter.Label(window, text=" This player is estimated to have " + str(predictions) + " minutes per game")
   final_mark.place(x=25, y=290)


# Creates the Tkinter window
window = tkinter.Tk()

# Assigns the dimensions of the window
window.geometry("316x324")

# Creates a label with text and then puts it at specific location
lbl1 = tkinter.Label(window, text="Please input all necessary information and then")
lbl1.place(x=35, y=0)

# Creates a label with text and then puts it at a specific location
lbl2 = tkinter.Label(window, text="click calculate to get predicted minutes per game for player!")
lbl2.place(x=0, y=20)

# Creating label alongside entry box in specific location
tkinter.Label(window, text="Goals Overall").place(x=35, y=60)
goals_overall = Entry(window)
goals_overall.place(x=150, y=60)

# Creating label alongside entry box in specific location
tkinter.Label(window, text="Assists Overall").place(x=35, y=90)
assists_overall = Entry(window)
assists_overall.place(x=150, y=90)

# Creating label alongside entry box in specific location
tkinter.Label(window, text="Yellow Cards Overall").place(x=35, y=120)
yellow_cards = Entry(window)
yellow_cards.place(x=150, y=120)

# Creating label alongside entry box in specific location
tkinter.Label(window, text="Red Cards Overall").place(x=35, y=150)
red_cards = Entry(window)
red_cards.place(x=150, y=150)

# Creating label alongside entry box in specific location
tkinter.Label(window, text="Appearances").place(x=35, y=180)
appearances = Entry(window)
appearances.place(x=150, y=180)

# Creating label alongside entry box in specific location
tkinter.Label(window, text="Age").place(x=35, y=210)
age = Entry(window)
age.place(x=150, y=210)

# Creating button that calls calculate function when clicked and placing it in specific location
b = Button(window, text="Calculate!", command=calculate)
b.place(x=125, y=250)

# Opening tab
window.mainloop()


