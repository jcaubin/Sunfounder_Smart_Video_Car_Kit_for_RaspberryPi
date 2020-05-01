#!/usr/bin/env python
import PCA9685 as servo
import time                # Import necessary modules
import os

channel = 1
currentPos = 315


def Map(x, in_min, in_max, out_min, out_max):
	return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def setup(busnum=None):
	global leftPWM, rightPWM, homePWM, pwm
	leftPWM = 130
	homePWM = 315
	rightPWM = 540
	offset =0	
	try:

		for line in open('config'):
			if line[0:8] == 'offset =':
				offset = int(line[9:-1])
	except Exception as inst:
		print('config error')
		print(os.getcwd())
		print(inst)
	leftPWM += offset
	homePWM += offset
	rightPWM += offset
	if busnum == None:
		pwm = servo.PWM()                  # Initialize the servo controller.

	else:
		pwm = servo.PWM(bus_number=busnum) # Initialize the servo controller.
	pwm.frequency = 50
	currentPos = homePWM

# ==========================================================================================
# Control the servo connected to channel 0 of the servo control board, so as to make the 
# car turn left.
# ==========================================================================================
def turn_left():	
	global leftPWM, currentPos
	print(f'left: current:{currentPos} left:{leftPWM}')
	for i in range(currentPos, leftPWM,-1):
		pwm.write(channel, 0, i)  # CH0
		time.sleep(0.001)
	currentPos = leftPWM

# ==========================================================================================
# Make the car turn right.
# ==========================================================================================
def turn_right():	
	global rightPWM, currentPos
	print(f'right: current:{currentPos} right:{rightPWM}')
	for i in range(currentPos, rightPWM):
		pwm.write(channel, 0, i)  # CH0
		time.sleep(0.001)
	currentPos=rightPWM

# ==========================================================================================
# Make the car turn back.
# ==========================================================================================

def turn(angle):	
	signal = Map(angle, 0, 180, leftPWM, rightPWM)
	print(f'turn: angle: {angle}; signal: {signal};')
	pwm.write(channel, 0, signal)

def home():	
	global homePWM, currentPos
	print(f'home: current:{currentPos} home:{homePWM}')
	if homePWM > currentPos:
		step = 1
	else:
		step = -1
	for i in range(currentPos, homePWM, step):
		pwm.write(channel, 0, i)  # CH0
		time.sleep(0.002)
	currentPos=homePWM

def calibrate(x):
	pwm.write(channel, 0, 450+x)

def test():
	pwm.debug=False
	home()
	time.sleep(1)
	while True:		
		turn_left()
		time.sleep(5)
		home()
		time.sleep(5)
		turn_right()
		time.sleep(5)
		home()
		time.sleep(5)
		turn(0)
		time.sleep(1)
		turn(45)
		time.sleep(1)
		turn(90)
		time.sleep(1)
		turn(135)
		time.sleep(1)
		turn(180)
		time.sleep(1)


if __name__ == '__main__':
	setup()
	home()
	try:
		test()
	except KeyboardInterrupt:
		pass


