from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Renders a web page with a button
    return render_template('./index.html')

@app.route('/execute-action', methods=['POST'])
def execute_action():
    # Extract data from request
    data = request.json

    if data['action'] == 'toggle_state':
        print("Toggle state")
        control_electronics()
    elif data['action'] == 'p5_click':
        leds = data['leds']
        color = data['color']
        print(leds)
        print(color)
        print("Click from p5")

    return jsonify({"status": "success"})

def control_electronics():
    pass
#    global curr_status
#    global led_strip
#    curr_status = (curr_status+1)%3
#    led_strip.colorWipe(DEFAULT_STATUS[curr_status])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
