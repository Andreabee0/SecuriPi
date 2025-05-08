import RPi.GPIO as GPIO       # Import Raspberry Pi GPIO library
import time                   # Import time library for delays

LDR_PIN = 27                
SAMPLES  = 20                 # Number of rapid samples for smoothing readings
DELAY    = 0.01               # Seconds to wait between each rapid sample

def setup_ldr():
    GPIO.setup(LDR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # Set LDR_PIN as input with internal pull-down so it reads LOW by default

def read_raw():
    count = 0                      # Initialize count of HIGH readings
    for _ in range(SAMPLES):       # Take SAMPLES fast readings
        count += GPIO.input(LDR_PIN)  # increment if pin is HIGH
        time.sleep(DELAY)             # brief pause between samples
    return 1 if count > SAMPLES//2 else 0
    # Return 1 (dark) if majority of samples were HIGH, else 0 (light)

def is_dark():
    val = read_raw()                # Get the raw reading
    if val:                         # If val==1, it's dark
        print("Light check: dark")  # Debug output
        return True                 # Indicate dark
    else:                           # If val==0, it's light
        print("Light check: light") # Debug output
        return False                # Indicate light
