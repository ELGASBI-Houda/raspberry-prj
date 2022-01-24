import time
from picamera import PiCamera
import RPi.GPIO as GPIO


#Define BUtton 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

#Definig led 
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

camera = PiCamera()
camera.start_preview()
GPIO.wait_for_edge(17, GPIO.FALLING)
camera.capture('/home/pi/image.jpg')
GPIO.output(8, GPIO.HIGH) # Turn on
time.sleep(2) # Sleep for 1 second
GPIO.output(8, GPIO.LOW) # Turn off
camera.stop_preview()