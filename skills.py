"""
This is the third page of the app and will allow the user
to choose three skills from the list.
"""

# rather than starting from scratch, taking everything from the stats file
from stats import *

window3 = tk.Toplevel(window2)

# new frame (just like old frames)
frame3 = tk.Frame(window3, bg="#4a4a4a", padx=10, pady=10)
frame3.pack(anchor='center')

# back arrow
backToStats = tk.Button(frame3, image=backArrow, width=30, height=15, borderwidth=0, bg='#4a4a4a', command=window2.deiconify)

# create frame for explanation
explainFrame3 = tk.Frame(frame3, padx=10, pady=10)
explainFrame3.grid(row=2, column=0, rowspan=8)

# text with Explanation
expLine1 = Explanation(explainFrame3, "Choose three skills for your character.",1,0)
expLine2 = Explanation(explainFrame3, "Your character must have exactly three skills to continue.",2,0)
expLine3 = Explanation(explainFrame3, "The skills available are different for each character class.",3,0)

def explainLines2():
  # function to display explanation text
  expLine1.label()
  expLine2.label()
  expLine3.label()

class SkillzCheck:
  # this class gives each skill and checkbox a unified look and feel
  def __init__(self, row):
    # skillName is the checkbox text, row is for grid placement
    self.x = row
    self.s = ""
    self.v1 = tk.IntVar()
  def showit(self):
    # displays checkbox and label
    # checkboxFrames = tk.Frame(frame3, padx=5, pady=5, bg='#4a4a4a')
    # checkboxFrames.grid(row=self.x, column=1)
    checkone = tk.Checkbutton(frame3, bg='#4a4a4a', variable=self.v1, onvalue=1, offvalue=0, padx=7, pady=7).grid(row=self.x, column=2)
    checkName = tk.Label(frame3, text=self.s, padx=5, bg='#4a4a4a', fg='white', wraplength=100).grid(row=self.x, column=1, sticky='e')
  def set_text(self,skillName):
    self.s=skillName
    

# going to declare all skills globally, so that they can be accessed globally
x=3 # "x" is the row that all checkboxes will start on

# declare variables and location on grid
skill1 = SkillzCheck(x)
skill2 = SkillzCheck(x+1)
skill3 = SkillzCheck(x+2)
skill4 = SkillzCheck(x+3)
skill5 = SkillzCheck(x+4)
skill6 = SkillzCheck(x+5)
skill7 = SkillzCheck(x+6)

def blankSkills():
  # wipes old skills to make way for new ones
  skill1.set_text("               ")
  skill2.set_text("               ")
  skill3.set_text("               ")
  skill4.set_text("               ")
  skill5.set_text("               ")
  skill6.set_text("               ")
  skill7.set_text("               ")  

def mobSkills():
  # sets text for the mobster skills
  skill1.set_text("Hand-to-hand combat")
  skill2.set_text("Persuasion")
  skill3.set_text("Shotgun certification")
  skill4.set_text("Pickpocketing")
  skill5.set_text("Accounting (nefarious)")
  skill6.set_text("First aid")
  skill7.set_text("Stealth")

def agentSkills():
  # sets text for the agent skills
  skill1.set_text("Interrogation")
  skill2.set_text("Forensics")
  skill3.set_text("Disguise")
  skill4.set_text("Stealth")
  skill5.set_text("Sharp shooting")
  skill6.set_text("Hand-to-hand combat")
  skill7.set_text("Lockpicking and safe-cracking")

def teeSkills():
  # sets text for the teetotaler skills
  skill1.set_text("Axe throwing")
  skill2.set_text("Bible knowledge")
  skill3.set_text("Singing voice")
  skill4.set_text("Persuasion")
  skill5.set_text("Business savvy")
  skill6.set_text("Intimidation")
  skill7.set_text("Trickery")

def showSkillz():
  # displays skills for chosen class
  skill1.showit()
  skill2.showit()
  skill3.showit()
  skill4.showit()
  skill5.showit()
  skill6.showit()
  skill7.showit()

def determine_Skillz():
  # determines the chosen class and displays appropriate skills
  if classy.get_class() == "mobster":
    mobSkills()
  else:
    if classy.get_class() == "agent":
      agentSkills()
    else:
      if classy.get_class() == "teetotal":
        teeSkills()
      else:
        if classy.get_class() == "Hello":
          blankSkills()


def return_total():
  # determines how many checkboxes are checked
  totalSkills = skill1.v1.get() + skill2.v1.get() + skill3.v1.get() + skill4.v1.get() + skill5.v1.get() + skill6.v1.get() + skill7.v1.get()
  return totalSkills


def to_printout():
  # command to next page
  if return_total() == 3:
    window3.withdraw()
    from lastPage import lastPage
    lastPage()
  else:
    messagebox.showerror('OH NO!!!', 'That is NOT 3 checkboxes. Try again.', parent=window3)

# button to go to next page
nextButton2 = tk.Button(frame3, text="Next", command=to_printout)
  
def skillsPage():
  windowsConfigs(window3)
  backToStats.grid(row=0, column=0, ipadx=0, ipady=0, padx=10, sticky='w')
  headerLabel(frame3, "CHOOSE YOUR SKILLS", 4)
  explainLines2()
  determine_Skillz()
  showSkillz()
  nextButton2.grid(row=11, columnspan=3)
