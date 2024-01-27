# import GPIO package
import RPi.GPIO as GPIO
import time
import random
print("pick a number and press Enter")
x = input()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) # GPIO4 is at pin 7
GPIO.setup(12, GPIO.OUT) # GPIO18 is at pin 12
# main routine
cols = ["red", "green"]
colseq = random.choices(cols, k = int(x))
try:
	# here the main behavior
	#for i in range(int(x)):
	for color in colseq:
		if color == "red":
			rdton = random.sample(list(range(1,50,1)),1)[0]/100
			GPIO.output(7,True) # RED ON
			time.sleep(rdton)
			GPIO.output(7, False) # RED OFF
			time.sleep(0.1)
		else:
			rdton = random.sample(list(range(1,50,1)),1)[0]/100
			GPIO.output(12, True) # GREEN ON
			time.sleep(rdton)
			GPIO.output(12, False) # GREEN OFF
			time.sleep(.1)
# execption for clean reset
except KeyboardInterrupt:
	# whatever should happen if keyboard interrupt
	print("Program ended by user")
except:
	# All other error that can happen
	print("Other exception occured!!!")
finally:
	GPIO.cleanup() # ensure clean exit
