import json
from flask import Flask, render_template

app = Flask(__name__)

# Function to load strike status data from JSON file
def load_strike_status():
    with open('strike_status.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    # Load strike status data
    strike_status = load_strike_status()
    return render_template('index.html', strike_status=strike_status)

if __name__ == '__main__':
    app.run(debug=True)
