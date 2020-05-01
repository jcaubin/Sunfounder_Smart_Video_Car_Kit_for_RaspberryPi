import PCA9685 as servo
import time

channel = 1
currentPos = 315

leftPWM = 150
homePWM = 315
rightPWM = 500

pwm = servo.PWM()
pwm.frequency = 50
currentPos = homePWM