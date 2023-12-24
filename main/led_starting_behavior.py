#!/usr/bin/env python3
from pi_led_strip.PiLedStrip import PiLedController
from flask import Flask, request, render_template, jsonify

# Variables
DEBUG = False
DEFAULT_STATUS = [
    (0, 0, 0),
    (20, 0, 0),
    (0, 20, 0),
    (0, 0, 20),
]
curr_status = 1

# Functions
app = Flask(__name__)

@app.route('/')
def index():
    # Renders a web page
    return render_template('./index.html')

@app.route('/execute-action', methods=['POST'])
def execute_action():
    # Extract data from request
    data = request.json

    if data['action'] == 'toggle_state':
        print("Toggle state")
        toggle_state()
    elif data['action'] == 'p5_click':
        print("Click from p5")

    return jsonify({"status": "success"})

def toggle_state():
    global curr_status
    global led_strip
    curr_status = (curr_status+1)%3
    led_strip.colorWipe(DEFAULT_STATUS[curr_status])

# Main program logic follows:
if __name__ == '__main__':
    led_strip = PiLedController(100)
    if DEBUG:
        try:
            led_strip.colorWipe((0, 0, 0), 10)
            while True:
                led_strip.colorWipe((20, 0, 0))  # Red wipe
                led_strip.colorWipe((0, 20, 0))  # Green wipe
                led_strip.colorWipe((0, 0, 20))  # Blue wipe
                #rainbow(strip)
                #rainbowCycle(strip)
                #theaterChaseRainbow(strip)
        except KeyboardInterrupt:
            if args.clear:
                colorWipe((0, 0, 0), 10)
    else:
        led_strip.colorWipe(DEFAULT_STATUS[curr_status])
        app.run(host='0.0.0.0', port=8080)
