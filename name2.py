from flask import Flask
from flask_restful import Api, Resource, reqparse, inputs


      

app = Flask(__name__)
api = Api(app)
print ("Done")


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


api.add_resource(Motor, "/motor/<int:motor_id>")

print ("Start")
if __name__ == "__main__":
    app.run(debug= True)
