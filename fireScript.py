# Jose Montanez
# Senior Design Tiny House
# This script handles the fire sensor

import RPi.GPIO as GPIO
import datetime
import time
import os

# This variable holds the delay time in seconds
# Change it if you want
SLEEP = 1

# To setup GPIO
# I'm using pin 40 which is GPIO21
pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

# This section checks to see oif an excel file has already been created
file = open("fireDetection.csv", "a")
if(os.path.getsize("fireDetection.csv") == 0):
    file.write("Time and date a fire was detected\nDate and TIme\tDetection\n") 
file.close()

def callback(pin):
    print("Flame detected")
    file = open("fireDetection.csv", "a")
    from datetime import datetime
    file.write(str(datetime.now()))
    file.write("\t")
    file.write("A fire was detected\n")
    file.close()
    
# Notifies when the pin goes high or low
GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime = 300)    
# Assigns function to the GPIO pin, runs the function when it changes
GPIO.add_event_callback(pin, callback)

# Loops forever
while True:
    time.sleep(SLEEP)