import RPi.GPIO as GPIO       # Import Raspberry Pi GPIO library
import time                   # Import time library for delays

PIR_PIN = 17                  

def setup_pir():
    GPIO.setup(PIR_PIN, GPIO.IN)       # Configure PIR_PIN as an input
    print("Calibrating PIR sensor...") # Inform user calibration is starting
    time.sleep(5)                      # Wait 5 seconds for PIR warm-up
    print("PIR Ready")                 # Inform user PIR is ready

def motion_detected():
    return GPIO.input(PIR_PIN)         # Return True if PIR detects motion, False if not
