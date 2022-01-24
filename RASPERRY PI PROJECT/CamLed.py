from picamera import PiCamera
import RPi.GPIO as GPIO

import time
camera = PiCamera()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

camera.start_preview()
for i in range(4):
    time.sleep(1)
    camera.capture('/home/pi/image%s.jpg' % i)
    GPIO.output(8, GPIO.HIGH) # Turn on
    time.sleep(1) # Sleep for 1 second
    GPIO.output(8, GPIO.LOW) # Turn off
camera.stop_preview()





