"""
Program Name: RPG Character Builder
Author: Mary Stromberg
Date started: 2-19-24
Purpose: allows a user to build their own RPG character based on a series of options.
"""

# importing all functions from last page
from skills import *

# run all functions
def main():
  classPage()
  statsPage()
  skillsPage()
  

if __name__=="__main__":
  main()

tk.mainloop()
