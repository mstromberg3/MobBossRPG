"""
Program Name: RPG Character Builder
Author: Mary Stromberg
Date started: 2-19-24
Purpose: allows a user to build their own RPG character based on a series of options.
"""
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
  window.geometry("400x400")
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

"""
def forget(widget):
  widget.forget()

def retrieve(widget): 
  widget.pack(fill = 'both', expand = True) 
  """

def labelConfig(label,x,y):
  # label configuration
  label_font = font.Font(size=12)
  label = tk.Label(frame1, text=label, bg='#4a4a4a', fg='white', font=label_font, wraplength=100, height=2)
  label.grid(row=x, column=y)

def buttonConfig(words,pic,x,y,s,e,d):
  # create and style button
  button = tk.Button(frame1, text=words, image=pic, width=100, height=100, command=lambda:[window2.deiconify(), re_reset(s,e,d)])
  button.grid(row=x,column=y, padx=10, pady=10)

def classPage():
  windowConfig()
  labelConfig("Choose your class",0,0)
  buttonConfig("Click Me", mobsterButton, 0,1,10,30,60)
  labelConfig("Mobster", 1,1)
  buttonConfig("No, click me",agentButton, 2,0,60,30,10)
  labelConfig("Secret Agent",3,0)
  buttonConfig("NO! ME!",teetotalerButton, 2,1,30,60,10)
  labelConfig("Teetotaler", 3,1)  

from stats import *

# run all functions
def main():
  classPage()
  window2.withdraw()
  statsPage()
  

if __name__=="__main__":
  main()

tk.mainloop()