from gpiozero import OutputDevice
from flask import Flask

app = Flask(__name__)

fanRelay = OutputDevice(16)

@app.route('/')
def main():
    return '<h3>Fan</h3><br><a href="/on">Turn On</a><br><a href="/off">Turn Off</a>'

@app.route('/on')
def on():
    fanRelay.on()
    return '<a href="/">Go Back</a>'

@app.route('/off')
def off():
    fanRelay.off()
    return '<a href="/">Go Back</a>'
