import RPi.GPIO as GPIO
from time import sleep
print(GPIO.VERSION)

LEDPin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPin, GPIO.OUT, initial=GPIO.LOW)
count = 0
while count < 5:
	GPIO.output(LEDPin, GPIO.HIGH)
	print("Led ON")
	sleep(3)
	GPIO.output(LEDPin, GPIO.LOW)
	print("Led OFF")
	sleep(3)
	count += 1
GPIO.cleanup()