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
    print("Electronics controlled!")  # Replace with your actual control code
    # Your code to control electronics goes here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
