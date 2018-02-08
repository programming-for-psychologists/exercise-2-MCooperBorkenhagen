#exercise 2 part 1
# Create a fixation cross using a TextStim object visual.TextStim set text to"+" and color to "white".
#Make the fixation cross appear for 500 ms before each name and disappears right before the name comes up.


import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

"""
the two line above are a more compact way of writing:
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixCross = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])
while True:
    nameShown = random.choice(firstNames)
    fixCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    if event.getKeys(['q']):
        break
