from tkinter import RIGHT
from flask import Flask
from flask_restful import Api, Resource, reqparse

import RPi.GPIO as GPIO
from time import sleep
       

app = Flask(__name__)
api = Api(app)
print ("Done")

Motor1A = 23  #DIR1
Motor1E = 24  #PWM1
Motor2A = 17  #DIR2
Motor2E = 27  #PWM2

def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)
        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)

def stop():
    print ("stop")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)

def forward():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    print ("Forward")

def back():
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    print ("Backward")

def left():
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    print ("left")

def right():
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    print ("right") 

motor_put_args = reqparse.RequestParser()
motor_put_args.add_argument("action1", type=str, help="Enter Robot's expected action")
motor_put_args.add_argument("action2", type=str, help="Enter Robot's expected action")
motor_put_args.add_argument("action3", type=str, help="Enter Robot's expected action")
motor_put_args.add_argument("action4", type=str, help="Enter Robot's expected action")
motor_put_args.add_argument("action5", type=str, help="Enter Robot's expected action")

motors = {}

class Motor(Resource):

    def get(self, motor_id):
        return motors[motor_id]

    def put(self, motor_id):
        args = motor_put_args.parse_args()
        motors[motor_id] = args
        return motors[motor_id], 201

if "action1" == "Right":
    right()
    sleep(2)
elif "action1"=="Left":
    left()
    sleep(2)
elif "action1"=="Forward":
    forward()
    sleep(2)
elif "action1"=="Backward":
    back()
    sleep(2)
else :
    stop()  
  

api.add_resource(Motor, "/motor/<int:motor_id>")
setup()
print ("Start")
if __name__ == "__main__":
    app.run(debug= True)
