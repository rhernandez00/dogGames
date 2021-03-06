#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), marzo 12, 2017, at 17:46
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
#from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import serial
import serial.tools.list_ports
import time
from sys import platform


raspberry = platform !='win32' #checks if it is running in windows

nTrials = 15


testing = False

ports = list(serial.tools.list_ports.comports())
intervalTime = 2.000000



#--- box parameters---

incorrectWidth = 0.35 
incorrectHeight = 0.35 
incorrectColor = [1,1,0]
incorrectTime = 5.0
intervalIncorrect = 0.5

correctColor = [0,0,1]
correctHeight = 0.6
correctWidth = 0.6 #max 2
correctTime = 5.0
intervalCorrect = 0.5


if testing:
    highV = 2
    lowV = 0
else:        
    highV = 2
    lowV = 0

for p in ports:
    if "CH340" in p[1]:
        strTmp = str(p)
        strTmp = strTmp[0:5]
        strTmp = strTmp.replace('COM','')
        nPort = 'com' + strTmp

#data = serial.Serial(nPort,9600,timeout=1)  
if testing:
    print 'Fake arduino on'
elif raspberry == 1:
    dataArduino = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
else:        
    dataArduino = serial.Serial('com8',9600,timeout=1)


def reward():
    global testing
    if testing:
        print 'reward'
    else:
        dataArduino.write(str(99))

def water():
    global testing
    if testing:
        print 'water'
    else:
        dataArduino.write(str(88))

def notifyError():
    global testing
    if testing:
        print 'error'
    else:
        dataArduino.write(str(77))
    

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'exp2'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': 'test'}
#dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
#if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=False,
    dataFileName=filename)
#save a log file for detail verbose info


# LOG experiment
#logFile = logging.LogFile(filename+'.log', level=logging.EXP)
#logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(800, 480), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg')

expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"




trialClock = core.Clock()
incorrectPol = visual.Rect(win=win, name='incorrectPol',
    width=[incorrectWidth, 2][0], height=[1, incorrectHeight][1],
    ori=0, pos=[-0.5, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=incorrectColor, fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
correctPol = visual.Rect(win=win, name='correctPol',
    width=[correctWidth, 2][0], height=[1, correctHeight][1],
    ori=0, pos=[0.5, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=correctColor, fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "correctFeed"
correctFeedClock = core.Clock()
rewardState = visual.Rect(
    win=win, name='rewardState',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "intervalInter"
intervalInterClock = core.Clock()
interTrialPol = visual.Rect(win=win, name='interTrialPol',
    width=[2, 2][0], height=[2, 2][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=nTrials, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    #choses from two possible positions a place to set the correct and incorrect
    side = randint(high=highV,low=lowV,size=1)
    if side == 0:
        correctPol.pos = [0.5,0]
        incorrectPol.pos = [-0.5,0]
    elif side == 1:
        correctPol.pos = [-0.5,0]
        incorrectPol.pos = [0.5,0]
    else:
        correctPol.pos = [-0.5,0]
        incorrectPol.pos = [-1,0]

    xCorrectMin = correctPol.pos[0] -correctWidth/2 
    xCorrectMax = correctPol.pos[0] +correctWidth/2
    yCorrectMin = correctPol.pos[1] -correctHeight/2 
    yCorrectMax = correctPol.pos[1] +correctHeight/2
    
    xIncorrectMin = incorrectPol.pos[0] -incorrectWidth/2 
    xIncorrectMax = incorrectPol.pos[0] +incorrectWidth/2
    yIncorrectMin = incorrectPol.pos[1] -incorrectHeight/2 
    yIncorrectMax = incorrectPol.pos[1] +incorrectHeight/2
    
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(incorrectPol)
    trialComponents.append(correctPol)
    trialComponents.append(mouse)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *incorrectPol* updates
        if t >= 0.0 and incorrectPol.status == NOT_STARTED:
            # keep track of start time/frame for later
            incorrectPol.tStart = t  # underestimates by a little under one frame
            incorrectPol.frameNStart = frameN  # exact frame index
            incorrectPol.setAutoDraw(True)
        
        # *correctPol* updates
        if t >= 0.0 and correctPol.status == NOT_STARTED:
            # keep track of start time/frame for later
            correctPol.tStart = t  # underestimates by a little under one frame
            correctPol.frameNStart = frameN  # exact frame index
            correctPol.setAutoDraw(True)
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t  # underestimates by a little under one frame
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(trialClock.getTime())
                # abort routine on response
                if ((x < xCorrectMax) & (x > xCorrectMin)) & ((y < yCorrectMax) & (y > yCorrectMin)):
                    continueRoutine = False
                elif ((x < xIncorrectMax) & (x > xIncorrectMin)) & ((y < yIncorrectMax) & (y > yIncorrectMin)):
                    continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x[0])
    trials.addData('mouse.y', mouse.y[0])
    trials.addData('mouse.leftButton', mouse.leftButton[0])
    trials.addData('mouse.midButton', mouse.midButton[0])
    trials.addData('mouse.rightButton', mouse.rightButton[0])
    trials.addData('mouse.time', mouse.time[0])
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    if ((x < xCorrectMax) & (x > xCorrectMin)) & ((y < yCorrectMax) & (y > yCorrectMin)):
        rewardState.fillColor = [0.,0.,1.]
        correctFeedback = correctTime
        reward()
        rewardReset = 1
        intervalTime = intervalCorrect
        #time.sleep(2)
        
    else:
        rewardState.fillColor = [0.8,0.,0.]
        correctFeedback = incorrectTime
        notifyError()
        intervalTime = intervalIncorrect
        #water()
        
    # ------Prepare to start Routine "correctFeed"-------
    t = 0
    correctFeedClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(correctFeedback)
    # update component parameters for each repeat
    # keep track of which components have finished
    correctFeedComponents = [rewardState]
    for thisComponent in correctFeedComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "correctFeed"-------
    while continueRoutine and routineTimer.getTime() > 0:
        #if (routineTimer.getTime() < 1.00000) and (rewardReset == 1):
            
        #    rewardReset = 0
        # get current time
        t = correctFeedClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rewardState* updates
        if t >= 0.0 and rewardState.status == NOT_STARTED:
            # keep track of start time/frame for later
            rewardState.tStart = t
            rewardState.frameNStart = frameN  # exact frame index
            rewardState.setAutoDraw(True)
        elif rewardState.status == STARTED and t >= (0.0 + correctFeedback):
            rewardState.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in correctFeedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "correctFeed"-------
    for thisComponent in correctFeedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)    
    #reward set to 0
    #dataArduino.write(str(rotTube))
    
    #------Prepare to start Routine "intervalInter"-------
    t = 0
    intervalInterClock.reset()  # clock 
    frameN = -1
    routineTimer.add(intervalTime)
    # update component parameters for each repeat
    # keep track of which components have finished
    intervalInterComponents = []
    intervalInterComponents.append(interTrialPol)
    for thisComponent in intervalInterComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "intervalInter"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = intervalInterClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *interTrialPol* updates
        if t >= 0.0 and interTrialPol.status == NOT_STARTED:
            # keep track of start time/frame for later
            interTrialPol.tStart = t  # underestimates by a little under one frame
            interTrialPol.frameNStart = frameN  # exact frame index
            interTrialPol.setAutoDraw(True)
        if interTrialPol.status == STARTED and t >= (0.0 + (intervalTime)): #most of one frame period left
            interTrialPol.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intervalInterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "intervalInter"-------
    for thisComponent in intervalInterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # LOG experiment
    #thisExp.nextEntry()
    time.sleep(2)
    
    
# completed X repeats of 'trials'
dataArduino.close()
win.close()
core.quit()
