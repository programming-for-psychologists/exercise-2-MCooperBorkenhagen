#exercise 2 part 8
#Extend the task by requiring the subject to respond by pressing a spacebar (the key is called 'space'),
#as quickly as possible anytime the name on the screen matches the name you entered into the box
#(so if I enter 'Gary' I would have to press 'space' anytime the name 'Gary' shows up.
#If the participant presses 'space' to the wrong name (false alarm), or misses the name (a miss), show a red X.



import time
import sys
import random
from psychopy import visual,event,core,gui



def errorWindow(text):
	errorDlg = gui.Dlg(title="Error", pos=(200,400))
	errorDlg.addText('Error: '+text, color='Red')
	errorDlg.show()



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


userVar = {'Name':'Enter your name'}
nameGiven = False
while not nameGiven:
    dlg = gui.DlgFromDict(userVar)
    if userVar['Name'] not in firstN:
        errorWindow('NAME DOES NOT EXIST')
    else:
        nameGiven = True
    if event.getKeys('q'):
        break


while nameGiven:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    currentName = random.choice(firstN)
    nameStim.setText(currentName)
    nameStim.draw()
    win.flip()
    if currentName == userVar['Name']:
        correct = ['space']
    else:
        correct = None
    resp = event.waitKeys(maxWait = tooLong, keyList = ['space'])
    if resp != correct:
        incorrectResp.draw()
        win.flip()
        core.wait(.50)
    if event.getKeys('q'):
        break
