#exercise2 part 5
#Now let's implement some feedback. Let's allow either a 'f' or 'l' response for each trial.
# If the response is correct, show a green 'O' before the start of the next trial. If the response is wrong,
#show a red 'X' (you can use textStim objects for feedback). Show the feedback for 500 ms.
#Note: we have someone in a class whose last name is a common first name.
#If this were an experiment, how might this affect responses?


import time
import sys
import random
from psychopy import visual,event,core, gui


names = open('names.txt', 'r').readlines()
firstN = [name.split(' ')[0] for name in names]
lastN = [name.split(' ')[1] for name in names]
allNames = firstN + lastN
win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixCross = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])
correctResp = visual.TextStim(win, text="0", height=40, color="green", pos=[0,0])
incorrectResp = visual.TextStim(win, text="X", height=40, color="red", pos=[0,0])


while True:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    currentName = random.choice(allNames)
    nameStim.setText(currentName)
    nameStim.draw()
    win.flip()
    keys = event.waitKeys(keyList=['f', 'l', 'q'])
    key = keys[0]
    if key == 'q':
        break
    isFirstName = (currentName in firstN)
    if (isFirstName and key == 'f') or (not isFirstName and key == 'l'):
        correctResp.draw()
    else:
        incorrectResp.draw()
    win.flip()
    core.wait(.5)
