#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on marzo 15, 2017, at 17:27
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'expDell'  # from the Builder filename that created this script
expInfo = {u'participant': u''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'D:\\dogGames\\expDell.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "initi"
initiClock = core.Clock()
green = visual.Rect(
    win=win, name='green',
    width=(1, 2)[0], height=(1, 2)[1],
    ori=0, pos=(-0.5, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[0,1,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
red = visual.Rect(
    win=win, name='red',
    width=(1, 2)[0], height=(1, 2)[1],
    ori=0, pos=(0.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "correctFeed"
correctFeedClock = core.Clock()
rewardState = visual.Rect(
    win=win, name='rewardState',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
bigLoop = data.TrialHandler(nReps=4, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='bigLoop')
thisExp.addLoop(bigLoop)  # add the loop to the experiment
thisBigLoop = bigLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBigLoop.rgb)
if thisBigLoop != None:
    for paramName in thisBigLoop.keys():
        exec(paramName + '= thisBigLoop.' + paramName)

for thisBigLoop in bigLoop:
    currentLoop = bigLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBigLoop.rgb)
    if thisBigLoop != None:
        for paramName in thisBigLoop.keys():
            exec(paramName + '= thisBigLoop.' + paramName)
    
    # ------Prepare to start Routine "initi"-------
    t = 0
    initiClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    # keep track of which components have finished
    initiComponents = [green, mouse, red]
    for thisComponent in initiComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "initi"-------
    while continueRoutine:
        # get current time
        t = initiClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *green* updates
        if t >= 0.0 and green.status == NOT_STARTED:
            # keep track of start time/frame for later
            green.tStart = t
            green.frameNStart = frameN  # exact frame index
            green.setAutoDraw(True)
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
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
                mouse.time.append(initiClock.getTime())
                # abort routine on response
                continueRoutine = False
        
        # *red* updates
        if t >= 0.0 and red.status == NOT_STARTED:
            # keep track of start time/frame for later
            red.tStart = t
            red.frameNStart = frameN  # exact frame index
            red.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in initiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "initi"-------
    for thisComponent in initiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for bigLoop (TrialHandler)
    if len(mouse.x): bigLoop.addData('mouse.x', mouse.x[0])
    if len(mouse.y): bigLoop.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): bigLoop.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): bigLoop.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): bigLoop.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): bigLoop.addData('mouse.time', mouse.time[0])
    # the Routine "initi" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "correctFeed"-------
    t = 0
    correctFeedClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    correctFeedComponents = [rewardState]
    for thisComponent in correctFeedComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "correctFeed"-------
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rewardState.status == STARTED and t >= frameRemains:
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
    thisExp.nextEntry()
    
# completed 4 repeats of 'bigLoop'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
