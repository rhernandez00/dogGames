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
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(800, 480), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
xCorrectMin = 0.25
xCorrectMax = 0.75
yCorrectMin = -0.25
yCorrectMax = 0.25


trialClock = core.Clock()
incorrectPol = visual.Rect(win=win, name='incorrectPol',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[-0.5, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
verdaderoPol = visual.Rect(win=win, name='verdaderoPol',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0.5, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,1,0], fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "correct"
correctClock = core.Clock()
verdaderoFeed = visual.Rect(win=win, name='verdaderoFeed',
    width=[0.8, 0.8][0], height=[0.8, 0.8][1],
    ori=0, pos=[-0.4, -0.4],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,1], fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
corrSound = sound.Sound('Correcto.wav', secs=-1)
corrSound.setVolume(1)

# Initialize components for Routine "incorrect"
incorrectClock = core.Clock()
falsoPol = visual.Polygon(win=win, name='falsoPol',
    edges = 90, size=[0.5, 0.5],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
sound_1 = sound.Sound(u'Incorrecto.wav', secs=-1)
sound_1.setVolume(1)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=8, method='random', 
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
    trialComponents.append(verdaderoPol)
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
        
        # *verdaderoPol* updates
        if t >= 0.0 and verdaderoPol.status == NOT_STARTED:
            # keep track of start time/frame for later
            verdaderoPol.tStart = t  # underestimates by a little under one frame
            verdaderoPol.frameNStart = frameN  # exact frame index
            verdaderoPol.setAutoDraw(True)
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
        
        #------Prepare to start Routine "correct"-------
        t = 0
        correctClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        correctComponents = []
        correctComponents.append(verdaderoFeed)
        correctComponents.append(corrSound)
        for thisComponent in correctComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        
        #-------Start Routine "correct"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = correctClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *verdaderoFeed* updates
            if t >= 0.0 and verdaderoFeed.status == NOT_STARTED:
                # keep track of start time/frame for later
                verdaderoFeed.tStart = t  # underestimates by a little under one frame
                verdaderoFeed.frameNStart = frameN  # exact frame index
                verdaderoFeed.setAutoDraw(True)
            if verdaderoFeed.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                verdaderoFeed.setAutoDraw(False)
            # start/stop corrSound
            if t >= 0.1 and corrSound.status == NOT_STARTED:
                # keep track of start time/frame for later
                corrSound.tStart = t  # underestimates by a little under one frame
                corrSound.frameNStart = frameN  # exact frame index
                corrSound.play()  # start the sound (it finishes automatically)
            if corrSound.status == STARTED and t >= (0.1 + (0.9-win.monitorFramePeriod*0.75)): #most of one frame period left
                corrSound.stop()  # stop the sound (if longer than duration)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in correctComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "correct"-------
        for thisComponent in correctComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        corrSound.stop() #ensure sound has stopped at end of routine
        
    else:
        #------Prepare to start Routine "incorrect"-------
        t = 0
        incorrectClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        incorrectComponents = []
        incorrectComponents.append(falsoPol)
        incorrectComponents.append(sound_1)
        for thisComponent in incorrectComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "incorrect"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = incorrectClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *falsoPol* updates
            if t >= 0.0 and falsoPol.status == NOT_STARTED:
                # keep track of start time/frame for later
                falsoPol.tStart = t  # underestimates by a little under one frame
                falsoPol.frameNStart = frameN  # exact frame index
                falsoPol.setAutoDraw(True)
            if falsoPol.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                falsoPol.setAutoDraw(False)
            # start/stop sound_1
            if t >= 0.1 and sound_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_1.tStart = t  # underestimates by a little under one frame
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.play()  # start the sound (it finishes automatically)
            if sound_1.status == STARTED and t >= (0.1 + (0.9-win.monitorFramePeriod*0.75)): #most of one frame period left
                sound_1.stop()  # stop the sound (if longer than duration)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in incorrectComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "incorrect"-------
        for thisComponent in incorrectComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_1.stop() #ensure sound has stopped at end of routine
        
        
    thisExp.nextEntry()
    
# completed 27 repeats of 'trials'

win.close()
core.quit()
