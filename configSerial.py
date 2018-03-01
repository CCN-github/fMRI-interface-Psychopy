'''
Configures fMRI interface

This script defines functions that you will need to call in your experiment script in order to synchronize your experiment with the MR scanner.

Tested on the GIfMI Siemens 3T TRIO (@UZ Gent).

David Wisniewski (david.wisniewski@ugent.be)
'''

import serial
import time
from psychopy import core, event

# Initialize scanner interface 
def init_scannerSync():
    global scannerSync
    scannerSync = serial.Serial('COM1',9600,timeout=1) # make sure you pick the right COM port here.
    if scannerSync.isOpen(): # check whether it is open 
        print 'Open: ' + scannerSync.portstr + ', baudrate: ' + str(scannerSync.baudrate)

# Wait until the scanner sends the first pulse
def waitForExptStartTrigger():
   event.clearEvents(eventType='keyboard') # remove any keys waiting in the queue
   while True:
        if (scannerSync.read() == '5'): # the MRI 'start' code
            print('MRI trigger received!')
            break # begin the experiment
        key = event.getKeys() # also check for a keyboard trigger (any key)
        if len(key) > 0:
            if key == ['escape']: core.quit() # escape allows us to exit manually
            break # else begin the experiment

# Close the scanner interface    
def close_scannerSync():
    scannerSync.close()
    print 'Closed serial port to MRI'
