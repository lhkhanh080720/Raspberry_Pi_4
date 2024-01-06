import RPi.GPIO as GPIO
from time import sleep
import keyboard

LEDPin = 40
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPin, GPIO.OUT)
count = 0

try:
	while count < 5:
		GPIO.output(LEDPin, True)
		print("Led ON")
		sleep(2)
		GPIO.output(LEDPin, False)
		print("Led OFF")
		sleep(2)
		if keyboard.is_pressed():
			print("OUT")
			GPIO.cleanup()
			break
finally:
	GPIO.cleanup()


