
# now creating the stats window (because I don't know how to do it in a separate doc)
from os import fsdecode
import tkinter as tk
from tkinter import HORIZONTAL, LEFT, TOP, font, messagebox 
from tkinter.ttk import *

window2 = tk.Toplevel()

# random color generator (for testing purposes)
import random

def random_color_generator():
    r = random.randint(0, 999999)
    return r

# frame config
frame2 = tk.Frame(window2, bg="#4a4a4a", padx=10, pady=10)
frame2.grid()
frame2.pack(anchor='center')

def window2Config():
  # window configuration
  window2.title("  RPG Character Builder")
  window2.geometry("400x400")
  window2.configure(bg='#4a4a4a', padx=10, pady=10)


# set icon image
icon = tk.PhotoImage(file = "icon.png")
window2.iconphoto(False, icon)

# back arrow
backArrow = tk.PhotoImage(file="back.png")
backToClass = tk.Button(frame2, image=backArrow, width=30, height=15, borderwidth=0, bg='#4a4a4a', command=lambda:[window2.withdraw()])

# header label
headFrame = tk.Frame(frame2, padx=5, pady=5, bg='#4a4a4a')
headFrame.grid(row=1, column=0, columnspan=2)
headLabel = tk.Label(headFrame, text="CHOOSE YOUR STATS", bg='white', fg='black', font=font.Font(size=14))

# create frame for explanation
explainFrame = tk.Frame(frame2, padx=10, pady=10)
explainFrame.grid(row=2, column=0, rowspan=3)

# Explanation class (this took FOREVER)
class Explanation:
  def __init__(self,label,row,column):
    self.l = label
    self.x = row
    self.y = column
  def label(self):
    tk.Label(explainFrame, text=self.l, font=font.Font(size=9),wraplength=150, height=3).grid(row=self.x, column=self.y)

# text within Explanation
line1_exp = Explanation("Choose a number for each stat using the slider.",1,0)
line2_exp = Explanation("All three numbers must add up to exactly 100 to move to next page.",2,0)
line3_exp = Explanation("Click \"Get Total\" to calculate current total.",3,0)
line4_exp = Explanation("Stats have been set to the default for your class.",4,0)
line5_exp = Explanation("You can set the stats to near-even numbers with the Reset button.",5,0)

def explainLines():
  # function to display Explanation text
  line1_exp.label()
  line2_exp.label()
  line3_exp.label()
  line4_exp.label()
  line5_exp.label()


# Config for each stat frame
class Stats:
  def __init__(self, slideValName, row, column):
    #slideValName is the skill name, row and column are for grid placement
    self.name = slideValName
    self.x = row
    self.y = column
    self.v1 = tk.DoubleVar()
  def showit(self):
    # determines content and layout of each instance
    statFrames = tk.Frame(frame2, bg="#4a4a4a", padx=10, pady=10)
    statFrames.grid(row=self.x, column=self.y)
    # v1 = tk.DoubleVar() # figure out how to make this a text entry too
    # label specs
    l1 = tk.Label(statFrames, text=self.name, bg='#4a4a4a', fg='white').grid(row=0, column=0, sticky='s')
    # slider specs
    s1 = tk.Scale(statFrames, variable=self.v1, from_=1, to=100, orient=HORIZONTAL, sliderlength=17).grid(row=1, column=0, padx=20, pady=5)


# define different stats
survivalSlider = Stats("Survival Instincts",2,1)
empathySlider = Stats("Empathy",3,1)
driveSlider = Stats("Drive",4,1)

# this next series of functions calclulates and displays total value of all sliders

def get_slider_vals():
  # get the value of each slider
  survivalVal = survivalSlider.v1.get()
  empathyVal = empathySlider.v1.get()
  driveVal = driveSlider.v1.get()
  # calculate total of all three
  totalVal = survivalVal + empathyVal + driveVal
  return totalVal


def show_total():
  # this function determines how the total of all sliders is displayed
  show = int(get_slider_vals()) # defining text for ShowVal label
  showVal.config(text=show, font=font.Font(size=15))
  if get_slider_vals() != 100: # this if-else shows the value in red if it's not 100 and green if it is
  # it also grays out the next button until totals add up to 100
    showVal.config(fg="red")
    nextButton.config(fg='#9a9a9a')
  else:
    showVal.config(fg="green")
    nextButton.config(fg='black')

# creating frame for buttons
buttonsFrame = tk.Frame(frame2, bg="#4a4a4a", padx=10, pady=10)
buttonsFrame.grid(row=6, column=0, columnspan=2, sticky='s')
# defining button and label for showing total
valButton = tk.Button(buttonsFrame, text="Get Total", command=show_total)
showVal = tk.Label(buttonsFrame, bg='#4a4a4a')

# reset button
def re_reset(s=33,e=34,d=33):
  # sets stats back to default
  survivalSlider.v1.set(s) # placeholder numbers. Will update with classes
  empathySlider.v1.set(e)
  driveSlider.v1.set(d)
  show_total()

re_resetButton = tk.Button(buttonsFrame, text="Reset", command=re_reset)

# configure button to move to next page
def to_skills():
  # if total is 100, moves to next page. If not, displays error
  if get_slider_vals() == 100: # still need to edit this to move to next page. Currently test placeholder
    buttonsFrame.config(bg="#"+str(random_color_generator()))
  else:
    messagebox.showerror('Program Error', 'Error: cannot move to next page until total equals 100')

nextButton = tk.Button(buttonsFrame, text="Next", fg='#9a9a9a', command=to_skills)

# put all buttons in one function
def bottomButtons():
  valButton.grid(row=0, column=0, padx=10, sticky='w')
  showVal.grid(row=0, column=1, padx=15, sticky='w')
  re_resetButton.grid(row=0, column=2, padx=10)
  nextButton.grid(row=0, column=3, padx=10, sticky='e')

"""
def labelConfig(label,x,y):
  # label configuration
  label_font = font.Font(size=12)
  label = tk.Label(frame2, text=label, bg='#4a4a4a', fg='white', font=label_font, wraplength=100, height=2)
  label.grid(row=x, column=y)

def buttonConfig(words,pic,x,y):
  # create and style button
  button = tk.Button(frame2, text=words, image=pic, width=100, height=100)
  button.grid(row=x,column=y, padx=10, pady=10)
  """

# run all functions
def statsPage():
  window2Config()
  backToClass.grid(row=0, column=0, ipadx=0, ipady=0, padx=10, sticky='w')
  headLabel.grid(row=0, column=0, ipadx=5, ipady=5, padx=10)
  explainLines()
  survivalSlider.showit()
  empathySlider.showit()
  driveSlider.showit()
  re_reset()
  bottomButtons()