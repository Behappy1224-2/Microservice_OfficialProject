from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Setup the GPIO pin for controlling the light
RELAY_PIN_1 = 17  # GPIO pin for IN1
RELAY_PIN_2 = 27  # GPIO pin for IN2
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN_1, GPIO.OUT)
GPIO.setup(RELAY_PIN_2, GPIO.OUT)

@app.route('/control_light', methods=['POST'])
def control_light():
    data = request.get_json()
    action = data.get('action')
    if action == 'turn on the light':
        GPIO.output(RELAY_PIN_1, GPIO.HIGH)  # Turn on relay channel 1
        return "Light turned on", 200
    elif action == 'turn off the light':
        GPIO.output(RELAY_PIN_1, GPIO.LOW)  # Turn off relay channel 1
        return "Light turned off", 200
    elif action == 'turn on another device':
        GPIO.output(RELAY_PIN_2, GPIO.HIGH)  # Turn on relay channel 2
        return "Another device turned on", 200
    elif action == 'turn off another device':
        GPIO.output(RELAY_PIN_2, GPIO.LOW)  # Turn off relay channel 2
        return "Another device turned off", 200
    else:
        return "Invalid action", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
