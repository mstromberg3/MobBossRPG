
from os import fsdecode
import tkinter as tk
from tkinter import HORIZONTAL, LEFT, TOP, font, messagebox 
from tkinter.ttk import *
window = tk.Tk()

# frame config
frame1 = tk.Frame(window, bg="#4a4a4a", padx=10, pady=10)
frame1.grid()
frame1.pack(side=TOP)

def windowConfig():
  # window configuration
  window.title("  RPG Character Builder")
  window.geometry("400x420")
  window.configure(bg='#4a4a4a', padx=10, pady=10)

# import image(s)
mobsterImage = tk.PhotoImage(file="mobsterImage.png")
agentImage = tk.PhotoImage(file="agentImage.png")
teetotalerImage = tk.PhotoImage(file="teetotalerImage.png")

# set icon image
icon = tk.PhotoImage(file = "icon.png")
window.iconphoto(False, icon)

# resize images to button size
mobsterButton = mobsterImage.subsample(3,3)
agentButton = agentImage.subsample(3,3)
teetotalerButton = teetotalerImage.subsample(3,3)

def headerLabel(frameName, headerText, columns):
  # header label
  headFrame = tk.Frame(frameName, padx=5, pady=10, bg='#4a4a4a')
  headFrame.grid(row=1, column=0, columnspan=columns)
  headLabel = tk.Label(headFrame, text=headerText, bg='white', fg='black', font=font.Font(size=14))
  headLabel.grid(row=0, column=0, ipadx=5, ipady=5, padx=10)

def labelConfig(label,x,y):
  # label configuration
  label_font = font.Font(size=12)
  label = tk.Label(frame1, text=label, bg='#4a4a4a', fg='white', font=label_font, wraplength=100, height=2)
  label.grid(row=x, column=y)

class MakeItClassy:
  # defines classname and character name
  def __init__(self,name):
    self.n=name
    self.yn = "No Name"
  def get_class(self):
    return self.n
  def set_class(self,name):
    self.n = name
  def set_character(self,character):
    self.yn = character
  def get_character(self):
    return self.yn
    

# default value for classy variable
classy = MakeItClassy("hello")

# frame and entry box for character name
entryFrame = tk.Frame(frame1, bg='#4a4a4a', padx=10, pady=10)
entryFrame.grid(row=2, column=0, rowspan=2)
enterLabel = tk.Label(entryFrame, text="Enter character name, then click on picture of choice", bg='#4a4a4a', fg='white', wraplength=180, font=font.Font(size=12))
enterName = tk.Entry(entryFrame, width=12)

class ClassyButton:
  # configure class choice buttons
  def __init__(self,pic,row,column,name):
    self.p=pic
    self.x=row
    self.y=column
    self.n=name
    self.yn = "No Name"
  def showButton(self):
    from skills import re_reset, determine_Skillz, showSkillz
    button=tk.Button(frame1, image=self.p, width=100, height=100, command=lambda:[window.withdraw(), classy.set_class(self.n),re_reset(), determine_Skillz(), showSkillz(), classy.set_character(enterName.get())]).grid(row=self.x, column=self.y, padx=10, pady=10)

mobButt=ClassyButton(mobsterButton,2,1,"mobster")
agentButt=ClassyButton(agentButton,4,0,"agent")
teeButt=ClassyButton(teetotalerButton,4,1,"teetotal")

def buttonConfig(pic,x,y,name):
  # create and style button
  button = tk.Button(frame1, image=pic, width=100, height=100, command=lambda:[window.withdraw()])
  button.grid(row=x,column=y, padx=10, pady=10)

def classPage():
  windowConfig()
  headerLabel(frame1,"CHOOSE YOUR CLASS",2)
  enterLabel.grid(row=0, pady=15)
  enterName.grid(row=1, pady=15)
  mobButt.showButton()
  labelConfig("Mobster", 3,1)
  agentButt.showButton()
  labelConfig("Secret Agent",6,0)
  teeButt.showButton()
  labelConfig("Teetotaler", 6,1)  
