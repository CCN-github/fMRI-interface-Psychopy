


"""
How to call the functions defined in configSerial.py in you main experiment script.

Also includes code to measure the timing of the first scanner pulse received. 

David Wisniewski (david.wisniewski@ugent.be)
"""

# import the scripts
import configSerial as conser  # Just make sure configSerial.py is in the same folder as this script.
from psychopy import clock

# right at the beginning of your experiment you need to initialize the scanner interface. 
# you only need to do that once. 
conser.init_scannerSync()

# at the beginning of each run, before the first trial is presented, let the computer wait for the first scanner pulse.
print('Wating for Scanner Pulse')
# this lets you measure the onset of all events in your experiment
fmriTimer = core.Clock() 
# wait for the first pulse to arrive
conser.waitForExptStartTrigger() 
# IMPORTANT: you need to log the exact time at which the first pulse was received. The timing of all other events in your experiment will be relative to this event. 
# the onset of all other events can also be measured using the same command: fmriTimer.getTime()
scanOn=fmriTimer.getTime() 
print('Scanner Pulse received')

# Right at the end of your experiment, close the scanner interface
conser.close_scannerSync()
   
    
