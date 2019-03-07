from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
import time

ledBlink = 21
sw = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledBlink, GPIO.OUT)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
ledState = False
timestampOld = 0

camera = PiCamera()
camera.resolution = (2592,1944)
camera.framerate = 15
#camera.start_preview()

while True:
        swState = GPIO.input(sw)
        #print(swState)
        if swState == True:
                t = time.localtime()
                timestamp = time.strftime('%b-%d_%H%M%S', t)
                if (timestamp == timestampOld):
                        timestamp = timestamp + 'a'
                #print(timestamp)
                camera.capture('/home/pi/Desktop/DP/'+ timestamp +'.jpg')
                GPIO.output(ledBlink, GPIO.HIGH)
                timestampOld = timestamp

        elif swState == False:
                GPIO.output(ledBlink, GPIO.LOW)


GPIO.output(ledBlink, GPIO.LOW)
#camera.stop_preview()
GPIO.cleanup()