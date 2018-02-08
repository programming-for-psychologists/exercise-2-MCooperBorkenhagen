#exercise 2 part 2
# Open names.txt to see what the names list looks like.
#Make the script show last names instead of first names (don't change the names.txt file).



import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names]
win = visual.Window([800,600],color="black", units='pix')
lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixCross = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])
while True:
    nameShown = random.choice(lastNames)
    fixCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    lastNameStim.setText(nameShown)
    lastNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    if event.getKeys(['q']):
        break
