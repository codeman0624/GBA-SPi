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


def SendButtonValue(channel):
  ser.write(str(channel).encode())
	
	
def ButtonMonitor():
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

	GPIO.add_event_detect(UP_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(DOWN_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(LEFT_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(RIGHT_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(START_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(SELECT_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(A_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(B_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(X_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(Y_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(L_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	GPIO.add_event_detect(R_BCM, GPIO.FALLING, callback = SendButtonValue, bouncetime = 200)
	
	while (ser.read() != 'Q'):
    time.sleep(0.05)
