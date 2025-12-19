from microbit import *
import machine
import utime

# Define the pins for the trigger and echo
# Example uses Pin 0 for Trig and Pin 1 for Echo (adjust as per your wiring)
TRIG_PIN = pin13
ECHO_PIN = pin14

def get_distance_cm():
    # Send a 10 microsecond HIGH pulse on the trigger pin to start ranging
    TRIG_PIN.write_digital(0)
    utime.sleep_us(2)
    TRIG_PIN.write_digital(1)
    utime.sleep_us(10)
    TRIG_PIN.write_digital(0)

    # Measure the duration of the echo pulse in microseconds
    # time_pulse_us waits for the echo pin to go HIGH and measures the duration
    duration = machine.time_pulse_us(ECHO_PIN, 1, 20000) # Timeout after 20000 us

    if duration > 0:
        # Speed of sound is approx 343 m/s or 0.0343 cm/us
        # Distance = (Time * Speed_of_Sound) / 2 (for one way)
        # distance in cm = (duration in us * 0.0343) / 2
        # Simplified: distance in cm = duration / 58 (approx)
        distance = duration / 58
        return int(distance)
    else:
        return 0 # Return 0 or some error value if no echo is received

# Ensure the echo pin has no pull
ECHO_PIN.set_pull(ECHO_PIN.NO_PULL)

while True:
    distance_val = get_distance_cm()
    display.scroll(str(distance_val) + " cm")
    sleep(1000) # Wait for 1 second between readings
