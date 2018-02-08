#exercise 1 part 6
#Now, instead of waiting for a response forever, let's implement a timeout.
#Show accuracy feedback as before, but now also show a red 'X' if no response is received for 1 sec
# (and go on to the next trial automatically following the feedback).



import time
import sys
import random
from psychopy import visual,event,core, gui


names = open('names.txt', 'r').readlines()
firstN = [name.split(' ')[0] for name in names]
lastN = [name.split(' ')[1] for name in names]
firstOrLast = [firstN, lastN]
win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixCross = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])
correctResp = visual.TextStim(win, text="0", height=40, color="green", pos=[0,0])
incorrectResp = visual.TextStim(win, text="X", height=40, color="red", pos=[0,0])
tooLong = 1

while True:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    nameType = random.choice(firstOrLast)
    currentName = random.choice(nameType)
    nameStim.setText(currentName)
    nameStim.draw()
    win.flip()
    resp = event.waitKeys(maxWait = tooLong, keyList = ['f', 'l'])
    if currentName in firstN:
        correct = ['f']
    if currentName in lastN:
        correct = ['l']
    if resp == correct:
        correctResp.draw()
        win.flip()
        core.wait(.50)
    else:
        incorrectResp.draw()
        win.flip()
        core.wait(.50)
    win.flip()
    core.wait(.50)
    if event.getKeys('q'):
        break
