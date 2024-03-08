"""
This is the last page of the app and shows everything the user has chosen so far.
"""

from skills import *

window4 = tk.Toplevel(window3)

# frame for new window
frame4 = tk.Frame(window4, bg='#4a4a4a', padx=10, pady=10)
frame4.pack(anchor='center')

# back arrow
backToSkills = tk.Button(frame4, image=backArrow, width=30, height=15, borderwidth=0, bg='#4a4a4a', command=lambda: [window3.destroy(), window2.deiconify()])

# resizing images for page
finalMobster = mobsterImage.subsample(2,2)
finalAgent = agentImage.subsample(2,2)
finalTeetotaler = teetotalerImage.subsample(2,2)

def your_image():
  # determines which image to use
  if classy.get_class() == "mobster":
    return finalMobster
  else:
    if classy.get_class() == "agent":
      return finalAgent
    else:
      if classy.get_class() == "teetotal":
        return finalTeetotaler
      else:
        return icon

def your_stats():
  # determines the stats chosen by user
  return ("Survival Instincts: {}%\nEmpathy: {}%\nDrive: {}%".format(survivalSlider.v1.get(),empathySlider.v1.get(),driveSlider.v1.get()))

def your_skills():
  # determines which skills were chosen
  # starting by creating an array of all skills
  allSkills = [skill1,skill2,skill3,skill4,skill5,skill6,skill7]
  yourSkills = [] # second array to hold chosen skills
  for skills in allSkills:
    if skills.v1.get() == 1:
      yourSkills.append(skills.s)
  # return a string based on choices
  return ("\n{}\n{}\n{}".format(yourSkills[0],yourSkills[1],yourSkills[2]))

# creates labels for each stat
showName = tk.Label(frame4, text=classy.get_character(), bg='#4a4a4a', fg='white', wraplength=180, font=font.Font(size=12))
showImage = tk.Label(frame4, bg='#4a4a4a', image=your_image(), width=180, height=180)
statsLabel = tk.Label(frame4, bg='#4a4a4a', fg='white', text="Stats:")
showStats = tk.Label(frame4, bg='#4a4a4a', fg='white',  text=your_stats())
skillsLabel = tk.Label(frame4, bg='#4a4a4a', fg='white', text="Skills:")
showSkills = tk.Label(frame4, bg='#4a4a4a', fg='white', text=your_skills())

def display_stats():
  # places information in frame
  showName.grid(row=2, column=0)
  showImage.grid(row=3, column=0, rowspan=4)
  statsLabel.grid(row=3, column=1)
  showStats.grid(row=4, column=1)
  skillsLabel.grid(row=5, column=1, sticky='s')
  showSkills.grid(row=6, column=1)

def lastPage():
  windowsConfigs(window4)
  backToSkills.grid(row=0, column=0, ipadx=0, ipady=0, padx=10, sticky='w')
  headerLabel(frame4, "YOUR CHARACTER", 4)
  display_stats()
