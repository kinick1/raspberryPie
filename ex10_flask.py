import RPi.GPIO as gp
import led18 as led
import ex09_select as db

gp.setmode(gp.BCM)
gp.setup(18,gp.OUT)

from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>index</h1>"

@app.route('/led/on')
def led_on():
#     led18.led_on()
    return "<h1>led on</h1>"

# /led/on 라우팅, 응답은 "led on"
# /led/off 라우팅, 응답은  "led off"

@app.route('/led/off')
def led_off():
#     led18.led_off()
    return "<h1>led off</h1>"

@app.route("/select")
def slt():
    r=db.select_db()
    return r
    
if __name__=="__main__":
    app.run(host='192.168.219.71', port=5000)