import RPi.GPIO as GPIO
import time

# GPIO setup
RELAY_PIN = 17  # Use GPIO17 (pin 11 on the Pi)
GPIO.setmode(GPIO.BCM)  # Set GPIO pin numbering
GPIO.setup(RELAY_PIN, GPIO.OUT)  # Set the relay pin as an output

def turn_on_light():
    GPIO.output(RELAY_PIN, GPIO.LOW)  # Relay ON (LOW closes the switch)
    print("Light is ON")

def turn_off_light():
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Relay OFF (HIGH opens the switch)
    print("Light is OFF")

try:
    # Test turning the light on and off
    turn_on_light()
    time.sleep(2)  # Keep the light on for 2 seconds
    turn_off_light()
finally:
    GPIO.cleanup()  # Clean up the GPIO pins
