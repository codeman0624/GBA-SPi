#!/bin/python
# Simple script for shutting down the raspberry Pi with a button

import RPi.GPIO as GPIO
import time
import os
import signal

UP_BCM = 26
DOWN_BCM = 13
LEFT_BCM = 16
RIGHT_BCM = 12
START_BCM = 22
SELECT_BCM = 27
A_BCM = 6
B_BCM = 5
X_BCM = 7
Y_BCM = 23
L_BCM = 17
R_BCM = 4

Button_lookup = {
  4: "R",
  5: "B",
  6: "A",
  7: "X",
  12: "Right",
  13: "Down",
  16: "Left",
  17: "L",
  22: "Start",
  26: "Up",
  27: "Select"
  }

#Use the Broadcom SOC Pin numbers
#Setup the pin with internal pullups enabled and Pin in reading mode
GPIO.setmode(GPIO.BCM)

# Our function on what to do when the button is pressed


def cleanup(signalnum=None, handler=None):
  GPIO.remove_event_detect(UP_BCM)
  GPIO.remove_event_detect(DOWN_BCM)
  GPIO.remove_event_detect(LEFT_BCM)
  GPIO.remove_event_detect(RIGHT_BCM)
  GPIO.remove_event_detect(START_BCM)
  GPIO.remove_event_detect(SELECT_BCM)
  GPIO.remove_event_detect(A_BCM)
  GPIO.remove_event_detect(B_BCM)
  GPIO.remove_event_detect(X_BCM)
  GPIO.remove_event_detect(Y_BCM)
  GPIO.remove_event_detect(L_BCM)
  GPIO.remove_event_detect(R_BCM)
  exit(0)

#define the function to be called on termination signals 
signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)


def Button_Monitor(channel):
    print Button_lookup.get(channel, "Invalid button")


GPIO.setup(UP_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOWN_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEFT_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(START_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SELECT_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(A_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(X_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Y_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(L_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(R_BCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(UP_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(DOWN_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(LEFT_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(RIGHT_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(START_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(SELECT_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(A_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(B_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(X_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(Y_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(L_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)
GPIO.add_event_detect(R_BCM, GPIO.FALLING, callback = Button_Monitor, bouncetime = 200)


# Now wait
while 1:
	time.sleep(0.05)
