import time                   # Import time library for delays and timestamping
import light_sensor           # Import our light-sensing module
import motion_sensor          # Import our motion-sensing module
import texter                 # Import our SMS/texting module
import RPi.GPIO as GPIO       # Import GPIO for pin cleanup
import file_writer            # Import file-writing module

GPIO.setmode(GPIO.BCM)        # Use Broadcom (BCM) GPIO pin numbering
CHECK_INTERVAL = 1            # Seconds between each sensor check
TEXT_INTERVAL  = 60           # Minimum seconds between SMS alerts

def main():
    try:
        light_sensor.setup_ldr()      # Prepare LDR GPIO pin
        motion_sensor.setup_pir()     # Prepare PIR GPIO pin
        file_writer.setup()

        last_text_time = 0            # Timestamp of last SMS sent
        motion_monitoring = False     # Track whether PIR is actively monitored

        while True:
            if light_sensor.is_dark():   # If it’s dark according to LDR
                if not motion_monitoring:
                    print("It's getting dark, activating motion sensor:")
                    motion_monitoring = True
                    print("Monitoring motion...")

                if motion_sensor.motion_detected():  # If PIR sees motion
                    print("Motion detected!")
                    now = time.time()                # Current timestamp
                    if now - last_text_time >= TEXT_INTERVAL:
                        file_writer.writeReport()         # Wrote to reports
                        print("Alert written!")
                        last_text_time = now         # Update last-sent time
                    else:
                        print("Motion Detected!")
                else:
                    print("No motion.")               # No motion this cycle

            else:                                  # If it’s light
                if motion_monitoring:
                    print("It's daytime again. Stopping motion monitoring.")
                    motion_monitoring = False
                else:
                    print("It's daytime. No need to monitor motion.")

            time.sleep(CHECK_INTERVAL)            # Pause before next loop

    except KeyboardInterrupt:
        print("Exiting program.")               # Handle Ctrl+C gracefully

    finally:
        GPIO.cleanup()                          # Reset all GPIO pins on exit

if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly
