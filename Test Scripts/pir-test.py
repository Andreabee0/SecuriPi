import RPi.GPIO as GPIO  #This is the raspberry pi GPIO (General Purpose I/O)
import time  #time library 

PIR_PIN = 17 #This is the pin were using in BCM, NOT board numbering

GPIO.setmode(GPIO.BCM) #sets to BCM numbering
GPIO.setup(PIR_PIN, GPIO.IN) # configures the PIR pin as input

print("Calibrating")
time.sleep(5) # This gives time for the sensor to 'warm up', should be 30 ish seconds
print("Ready")

try:
    while True: # Infinit loop
        if GPIO.input(PIR_PIN): #if motion is detected, we output info 
            print("Motion")
        else: # if theres no motion, print just dots
            print("...")
        time.sleep(0.5) # refrshed every half second
except KeyboardInterrupt:
    print("Exiting") # This just makes Ctrl + C break the loop
finally:
    GPIO.cleanup() # Wipes info from the pins, a built in cleanup method