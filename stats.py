"""
this document is for the stats page and includes all functions and classes necessary to run that page (or they are imported)
"""
from classes import *

window2 = tk.Toplevel(window)

# frame config
frame2 = tk.Frame(window2, bg="#4a4a4a", padx=10, pady=10)
frame2.grid(row=0, column=0)
# frame2.pack(anchor='center')

def windowsConfigs(windowName):
  # window configuration
  windowName.title("  RPG Character Builder")
  windowName.geometry("400x420")
  windowName.configure(bg='#4a4a4a', padx=10, pady=10)
  icon = tk.PhotoImage(file = "icon.png")
  windowName.iconphoto(False, icon)

def backClassCmd():
  # brings back main window
  window.deiconify()
  classy.set_class("Hello")
  from skills import determine_Skillz
  determine_Skillz()

# back arrow
backArrow = tk.PhotoImage(file="back.png")
backToClass = tk.Button(frame2, image=backArrow, width=30, height=15, borderwidth=0, bg='#4a4a4a', command=backClassCmd)

# create frame for explanation
explainFrame = tk.Frame(frame2, padx=10, pady=10)
explainFrame.grid(row=2, column=0, rowspan=3)

# Explanation class (this took FOREVER)
class Explanation:
  def __init__(self,frameName,label,row,column):
    self.l = label
    self.x = row
    self.y = column
    self.f = frameName
  def label(self):
    tk.Label(self.f, text=self.l, font=font.Font(size=9),wraplength=150, height=3).grid(row=self.x, column=self.y)

# text within Explanation
line1_exp = Explanation(explainFrame,"Choose a number for each stat using the slider.",1,0)
line2_exp = Explanation(explainFrame, "All three numbers must add up to exactly 100 to move to next page.",2,0)
line3_exp = Explanation(explainFrame, "Click \"Get Total\" to calculate current total.",3,0)
line4_exp = Explanation(explainFrame, "Stats have been set to the default for your class.",4,0)
line5_exp = Explanation(explainFrame, "You can set the stats to near-even numbers with the Reset button.",5,0)

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
    #slideValName is the stat name, row and column are for grid placement
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
    l1 = tk.Label(statFrames, text=self.name, font=font.Font(size=10, weight='bold'), bg='#4a4a4a', fg='white').grid(row=0, column=0, sticky='s')
    # slider specs
    s1 = tk.Scale(statFrames, variable=self.v1, from_=1, to=100, orient=HORIZONTAL, length=150, sliderlength=17).grid(row=1, column=0, padx=5, pady=5)
    """ # can't get this section to work
    # entry box specs
    enterVal = tk.Entry(statFrames, width=4)
    enterVal.grid(row=2, pady=5)
    def setVal(self):
      enterValFloat = float(enterVal.get())
      self.v1.set(enterValFloat)
    enterVal.bind('<Return>', 'setVal')
    """


# define different stats
survivalSlider = Stats("Survival Instincts",2,1)
empathySlider = Stats("Empathy",3,1)
driveSlider = Stats("Drive",4,1)

# these next two functions calclulate and display total value of all sliders

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
def re_reset():  
  # sets stats to default for each class
  if classy.get_class()=="mobster":
    survivalSlider.v1.set(10)
    empathySlider.v1.set(30)
    driveSlider.v1.set(60)
  else:
    if classy.get_class()=="agent":
      survivalSlider.v1.set(20)
      empathySlider.v1.set(10)
      driveSlider.v1.set(70)
    else:
      if classy.get_class()=="teetotal":
        survivalSlider.v1.set(5)
        empathySlider.v1.set(47)
        driveSlider.v1.set(48)
      else:
        survivalSlider.v1.set(33)
        empathySlider.v1.set(34)
        driveSlider.v1.set(33)    
  show_total()

re_resetButton = tk.Button(buttonsFrame, text="Reset", command=re_reset)

# configure button to move to next page
def to_skills():
  # if total is 100, moves to next page. If not, displays error
  if get_slider_vals() == 100: # still need to edit this to move to next page. Currently test placeholder
    window2.withdraw()
    # buttonsFrame.config(bg="#"+str(random_color_generator()))
  else:
    messagebox.showerror('Program Error', 'Error: cannot move to next page until total equals 100', parent=window2)

nextButton = tk.Button(buttonsFrame, text="Next", fg='#9a9a9a', command=to_skills)

# put all buttons in one function
def bottomButtons():
  valButton.grid(row=0, column=0, padx=10, sticky='w')
  showVal.grid(row=0, column=1, padx=15, sticky='w')
  re_resetButton.grid(row=0, column=2, padx=10)
  nextButton.grid(row=0, column=3, padx=10, sticky='e')

# run all functions
def statsPage():
  windowsConfigs(window2)
  backToClass.grid(row=0, column=0, ipadx=0, ipady=0, padx=10, sticky='w')
  headerLabel(frame2, "CHOOSE YOUR STATS", 2)
  explainLines()
  survivalSlider.showit()
  empathySlider.showit()
  driveSlider.showit()
  re_reset()
  bottomButtons()
