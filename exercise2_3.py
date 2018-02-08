#exercise2 part 3
# Make the program randomly alternate between first names and last names.



import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
nameIndex = (0,1)
names = [name.split(' ')[random.choice(nameIndex)] for name in names]
win = visual.Window([800,600],color="black", units='pix')
lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixCross = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])
while True:
    nameShown = random.choice(names)
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
