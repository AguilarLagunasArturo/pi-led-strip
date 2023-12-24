#!/usr/bin/env python3
from pi_led_strip.PiLedStrip import PiLedController
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Renders a web page with a button
    return render_template('./index.html')

@app.route('/execute-action', methods=['POST'])
def execute_action():
    # Replace with your function to control electronics
    control_electronics()
    return jsonify({"status": "success"})

def control_electronics():
    global curr_status
    global led_strip
    curr_status = (curr_status+1)%3
    led_strip.colorWipe(DEFAULT_STATUS[curr_status])
    print("Electronics controlled!")  # Replace with your actual control code
    # Your code to control electronics goes here

DEBUG = False
DEFAULT_STATUS = [
    (0, 0, 0),
    (20, 0, 0),
    (0, 20, 0),
    (0, 0, 20),
]
cur_status = 1

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
