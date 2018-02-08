# exercise 2 part 10
#Output the response times (in ms, e.g., 453 for 453 ms) and accuracy (1 for correct, 0 for incorrect) to a
# file output.txt. Output one line per trial: each line should contain the accuracy (1 or 0) and the response
# time (in milliseconds). See the python documentation for examples of how to write to a file.
#Ask for help if you are stuck.




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

named=userVar['Name']
fileName=str(named)+'.txt'
dataFile=open(fileName, 'w')

while nameGiven:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    currentName = random.choice(firstN)
    nameStim.setText(currentName)
    nameStim.draw()
    win.flip()
    respClock=core.Clock()
    if currentName == userVar['Name']:
        correct = ['space']
    else:
        correct = None
    resp = event.waitKeys(maxWait = tooLong, keyList = ['space'])
    rt = str(respClock.getTime())
    if resp != correct:
        incorrectResp.draw()
        win.flip()
        core.wait(.50)
        accuracy = '0'
    else:
        accuracy = '1'
    if resp:
        print(rt)
        respClock.reset()
    if event.getKeys('q'):
        break
    data=('\t'.join([accuracy, rt]) +'\n')
    dataFile.write(data)
