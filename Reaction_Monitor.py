import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(6,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)

#define variables
start = 0
target_list = []
target = 0
reaction = 0.000

#adjustable variables
max_targets = 3
max_delay = 6
min_delay = 2

#create list of targets according to max number of targets
for i in range(max_targets):
    target_list.append(i + 1)

def assign_target():
    #delay for a random amount of time before choosing target
    delay = random.randrange(min_delay*1000, max_delay*1000, 1)/1000
    time.sleep(delay)
    #randomly assign target from list of possible targets
    new_target = random.choice(target_list)
    return new_target

def calc_reaction():
    #record start time
    start = time.time()
    
    while True:
        #read sensors
        status = [GPIO.input(4), GPIO.input(5), GPIO.input(6), GPIO.input(22), GPIO.input(23), GPIO.input(24), GPIO.input(25)]
        
        if status[target - 1] == 1:
            break
    
    new_reaction = time.time() - start
    return new_reaction

def start_stop():
    #start/stop monitoring if sensor 1 is held for 3 seconds
    return start
    
try:
    #main loop
    while True:
        target = assign_target()
        print(target)
        reaction = calc_reaction()
        print("%.3f" % (reaction))
        target = 0
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()


