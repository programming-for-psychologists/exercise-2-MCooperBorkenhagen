#exercise2 part 7
#Pop up a box that accepts a first name, and check to make sure that the name exists.
#If it doesn't, pop-up a 'Name does not exist'error box

import time
import sys
import random
from psychopy import visual,event,core, gui


def errorWindow(text):
	errorDlg = gui.Dlg(title="Error", pos=(200,400))
	errorDlg.addText('Error: '+text, color='Red')
	errorDlg.show()

names = open('names.txt', 'r').readlines()
firstN = [name.split(' ')[0] for name in names]
lastN = [name.split(' ')[1] for name in names]
firstOrLast = [firstN, lastN]
win = visual.Window([800,600],color="black", units='pix')

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
