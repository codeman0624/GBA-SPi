#!/bin/python
# Simple script for shutting down the raspberry Pi with a button

import RPi.GPIO as GPIO
import time
import os
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('/home/pi/GBA-SPi/BatteryMonitor/battery_monitor.config') #read the contents of the config file
SAVESTATE = config.get('save_state', 'Save')

#Use the Broadcom SOC Pin numbers
#Setup the pin with internal pullups enabled and Pin in reading mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def Shutdown(channel):
	if SAVESTATE == 'Y':
		#do a save state thing here
		#os.system("xdotool key "Shift_R+r"")
	os.system("sudo shutdown -h now")

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(20, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

# Now wait
while 1:
	time.sleep(1)

