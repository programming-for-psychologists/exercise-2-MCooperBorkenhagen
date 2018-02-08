#exercise2_4.py
#On each presentation of a name, wait for a response ('f' for first name, 'l' for last-name)
#and only proceed to the next name if the response is correct.
#Hint: if you've done steps 2-3 properly, this should be really easy.
#Refer to the psychopy documentation of event.waitKeys() if you have trouble.




import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
firstN = [name.split(' ')[0] for name in names]
lastN = [name.split(' ')[1] for name in names]
nameChoice = [firstN, lastN]
win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixCross = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])

while True:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    nameType = random.choice(nameChoice)
    nameShown = random.choice(nameType)
    nameStim.setText(nameShown)
    nameStim.draw()
    win.flip()
    if nameShown in firstN:
        event.waitKeys(keyList = 'f')
    if nameShown in lastN:
        event.waitKeys(keyList = 'l')
    win.flip()
    core.wait(.15)
    if event.getKeys(['q']):
        break
