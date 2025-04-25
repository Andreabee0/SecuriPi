import RPi.GPIO as GPIO   # GPIO library
import time            # time library 

# GPIO pin (BCM numbering)
LDR_PIN = 27

# Use BCM pin-numbering scheme
GPIO.setmode(GPIO.BCM)

print("Calibrating LDR sensor—keep, keep light level constant...")
# Give the circuit a second to 'warm up' anbd calibrate
time.sleep(5)
print("Ready")

def read_light_level():
    """"
    Charges the node, then switches to input and measures how long
    it stays HIGH before discharging through the LDR.
    Returns the discharge time in seconds.
    """
    # Charge the node 
    GPIO.setup(LDR_PIN, GPIO.OUT)
    GPIO.output(LDR_PIN, GPIO.HIGH)
    time.sleep(0.1)  # allow capacitor to charge

    # Switch to input and time until it discharges to LOW
    GPIO.setup(LDR_PIN, GPIO.IN)
    start = time.perf_counter()
    while GPIO.input(LDR_PIN) == GPIO.HIGH:
        # safety timeout after 1 second
        if time.perf_counter() - start > 1.0:
            break
    return time.perf_counter() - start

try:
    # Infinite loop 
    while True:
        dt = read_light_level()
        # Decide “light” vs “dark” based on the light, for now youll see 1 sec disharge when theres no light, and 0 sec discharge whith light
        if dt < 0.5:                                   #We can adjust this to be more specific, right now its just agressive darkness and agressive light
            print(f"{time.strftime('%H:%M:%S')} → Light: {dt:.3f} s")
        else:   #The two statements above and below will output the system time, and if its dark or light, as well as discharge time                                                               
            print(f"{time.strftime('%H:%M:%S')} → Dark : {dt:.3f} s")
        time.sleep(1)

except KeyboardInterrupt:
    # Ctrl+C to exit
    print("Exiting LDR test.")

finally:
    # Reset pins when done
    GPIO.cleanup()
