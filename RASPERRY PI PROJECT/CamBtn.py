import time
from picamera import PiCamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

camera = PiCamera()
camera.start_preview()
GPIO.wait_for_edge(17, GPIO.FALLING)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()