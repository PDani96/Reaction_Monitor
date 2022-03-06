import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.IN)

try:
    while True:
        #take a reading
        input = GPIO.input(6)
        
        if (input):
            print("Under Pressure")
        else:
            print("--------------")
        #slight pause
        #time.sleep(0.10)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
