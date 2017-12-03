 #!/usr/bin/env python
          
      
import time
import serial
import os
import signal
import ConfigParser
          

config = ConfigParser.ConfigParser()
config.read('/home/pi/GBA-SPi/BatteryMonitor/battery_monitor.config')				#read the contents of the config file
#configfile = open('/home/pi/GBA-SPi/BatteryMonitor/battery_monitor.config', 'w')	#open a file of the same name, for writing back to later
		  
PNGVIEWPATH = "/home/pi/GBA-SPi/BatteryMonitor/Pngview/"
ICONPATH = "/home/pi/GBA-SPi/BatteryMonitor/icons"
XOFFSET = config.get('offset_values', 'X')
YOFFSET = config.get('offset_values', 'Y')
CurrentPicture = "Current"
NewPicture = "New"
DISPLAY = "OFF"

#put these up here in case the thresholds want to be changed
BATTERYLOW = 10
BATTERY25 = 25
BATTERY50 = 50
BATTERY75 = 75
BATTERY100 = 100
BATTERYCHARGING = 101

		  
      
ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate = 19200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
#	timeout=1							#timeout every second, so other things can be serviced if necessary
)

#clean up the serial port, configuration file, and PNGview process when exiting
def cleanup(signalnum=None, handler=None):
	ser.flushInput()  
	ser.close()  #close the serial port
#	config.write(configfile)	#write the configurations back to the file
#	configfile.close()			#close the config file
	KillPNGView()
	exit(0)

#define the function to be called on termination signals 
signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)

def SetIcon(charge):
	global NewPicture
	global CurrentPicture

	if ord(charge) == 0:
		NewPiture = "LowCharge"
	elif ord(charge) <= BATTERYLOW:
		NewPicture = "LowCharge"	#names of the battery picture files
	elif ord(charge) <= BATTERY25:
		NewPicture = "charge25"
	elif ord(charge) <= BATTERY50:
		NewPicture = "charge50"
	elif ord(charge) <= BATTERY75:
		NewPicture = "charge75"
	elif ord(charge) <= BATTERY100:
		NewPicture = "charge100"
	else:
		NewPicture = "charging"
		
	
	#if the new picture is different from the current picture, then display it, otherwise do nothing
	if NewPicture != CurrentPicture:
		CurrentPicture = NewPicture		#update the current picture
		
		#only update the display if we want it on
		if DISPLAY == "ON":
			UpdateDisplay()


def UpdateDisplay():
	KillPNGView() #kill them all to remove the battery indicator, causes the icon to flash but i dont' care
				  #  maybe eventually change this to add the new battery icon, then kill just the old ones?
				  #Not sure I care enough about the icon flashing
	os.system(PNGVIEWPATH + "/pngview -b 0 -l 99999 -x " + str(XOFFSET) + " -y " + str(YOFFSET) + " " + ICONPATH + "/" + NewPicture + ".png &")
		
	
def SetDisplay(ON_OFF):
	global DISPLAY
#	print ord(ON_OFF)
	if ord(ON_OFF) == 0:
		DISPLAY = "OFF"
		KillPNGView()	#kill all the pngview processes to clear the screen
	else:
		DISPLAY = "ON"
		UpdateDisplay()
	

	
	
def KillPNGView():
	#print("killed all")
	os.system("sudo killall -q pngview")
	

#only an 8-bit bus, but offsets can be higher than 255, so
# split the high and low bits of the offset for transmitting,
# and stitch the full number back together here
def	SetXOFFSET(offset_high, offset_low):
	global XOFFSET
	XOFFSET = (ord(offset_high)*256) + ord(offset_low)
#	config.set('offset_values', 'X', XOFFSET)	#update the config with the new value
	UpdateDisplay()
#	print XOFFSET

def	SetYOFFSET(offset_high, offset_low):
	global YOFFSET
	YOFFSET = (ord(offset_high)*256) + ord(offset_low)
#	config.set('offset_values', 'Y', YOFFSET)	#update the config with the new value
	UpdateDisplay()
	



ser.flushInput()	#flush the input of everything
while (ser.read() != 'E'):  #wait here for the echo, use this to sync with the microcontroller 
	pass
	
#Run this forever basically

#The serial port will read string commands coming from the microcontroller
#The commands follow this syntax:
#Command Arg1 Arg2
#but all values are just integers, or ASCII characters only
while 1:
	commands = []	#create and clear my array for reading in the commands
	i = 0			#index counter
	
	#need to do an initial serial read, then keep checking if the
	#  read value is 'Q', for Quit.  Otherwise keep reading.  'Q' ends the command array
	commands.append(ser.read())		#need to just keep appending to the array
	
	while commands[i] != 'Q':
#		print commands		#here for debug
		commands.append(ser.read())	
		i+=1		#because i++ doesn't exist...?! dumb


	#'S' for shutdown
	if commands[0] == 'S':
		cleanup()
	#'I' for icon change, the next value is the battery value integer
	# greater than 100 means plugged in
	elif commands[0] == 'I':
		SetIcon(commands[1])	#sets the proper battery icon based off the number sent
	#'D' for display setting, next value is 'Y' or 'N', followed by battery value
	elif commands[0] == 'D':
		#the command must be ['D', 'Y']
		SetDisplay(commands[1])	#turns the battery display on or off
	#'X' for setting the X offset, next value is pixel offset
	elif commands[0] == 'X':
		SetXOFFSET(commands[1], commands[2])
	#'Y' for setting the Y offset, next value is pixel offset
	elif commands[0] == 'Y':
		SetYOFFSET(commands[1], commands[2])
	#'E' for echo, to check if the Pi is alive
	elif commands[0] == 'E':	
		ser.write('e')
#	else:
		#do nothing in the else case, that means the read timed out because nothing was sent
