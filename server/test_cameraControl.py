import PCA9685 as pca
import time  # Import necessary modules

panServo = 14
tilServo = 15
currentPanPos = 0
currentTilPos = 0

leftPWM = 130
homePWM = 315
rightPWM = 540

#controladora pwm
pwm = pca.PWM()
pwm.frequency = 50

ms = 0.3


def Map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) +
               out_min)


def pan(angle):
    if -75 <= angle <= 80:
        global currentPanPos
        signal = Map(angle + 90 - 4, 0, 180, leftPWM, rightPWM)
        print(f'turn: angle: {angle}; signal: {signal};')
        pwm.write(panServo, 0, signal)
        currentPanPos = angle


def tilt(angle):
    if -20 <= angle <= 90:
        global currentTilPos
        signal = Map(angle + 90 - 8, 0, 180, leftPWM, rightPWM)
        print(f'turn: angle: {angle}; signal: {signal};')
        pwm.write(tilServo, 0, signal)
        currentTilPos = angle


def slowPan(angle):
    if angle > currentPanPos:
        step = 1
    else:
        step = -1
    for a in range(currentPanPos, angle, step):
        pan(a)
        time.sleep(0.051)


def moveUp():
    tilt(currentTilPos + ms)


def moveDown():
    tilt(currentTilPos - ms)


def moveLeft():
    pan(currentPanPos + ms)


def moveRigth():
    pan(currentPanPos - ms)


def home():
    pan(0)
    tilt(0)


if __name__ == '__main__':
    home()
    slowPan(80)
    time.sleep(0.5)
    home()
    time.sleep(0.5)
    slowPan(-75)
    time.sleep(0.5)
    home()
    time.sleep(0.5)
    tilt(90)
    time.sleep(0.5)
    tilt(0)
    time.sleep(0.5)
    tilt(-20)
    time.sleep(0.5)
    home()