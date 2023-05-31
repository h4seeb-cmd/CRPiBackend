# import requests
# from flask import request
# import traceback
# from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
# from flask_restful import Api, Resource # used for REST API building
# from flask_cors import CORS  



# binary_api = Blueprint('binary_api', __name__,
#                    url_prefix='/api/binary')

# # API docs https://flask-restful.readthedocs.io/en/latest/api.html
# api = Api(binary_api)


# CORS(binary_api, methods=['GET', 'POST'], origins = '*')

# class BinaryAPI:
#     class binThing(Resource):
#         def post(self):
#                 endpoint = "http://127.0.0.1:4000/mediumish-theme-jekyll/powerful-things-markdown-editor/"
#                 body = request.get_json()
#                 number = body.get("tag")
#                 data = {
#                     "tag": number
#                 }
                
#                 try:
#                     response = requests.post(endpoint, json=data, headers={'Content-Type': 'application/json'})
#                     if response.status_code == 200:
#                         return response.json()  # Assuming the response is in JSON format
#                     else:
#                         return {"error": "Request failed"}, response.status_code
#                 except Exception:
#                     print(traceback.format_exc())
#                     return {"error": "Internal server error"}, 500
        
#         def get(self):
#             message = "example msg"
#             return message
        
#     api.add_resource(binThing, '/', methods=['GET', 'POST'])  # Added variable <query> to the route

# import requests
# from flask import request
# import traceback
# from flask import Blueprint, jsonify
# from flask_restful import Api, Resource
# from flask_cors import CORS

# binary_api = Blueprint('binary_api', __name__, url_prefix='/api/binary')
# api = Api(binary_api)

# CORS(binary_api, methods=['GET', 'POST'], origins='*')

# class BinaryAPI:
#     class binThing(Resource):
#         def post(self):
#             endpoint = "http://127.0.0.1:4000/mediumish-theme-jekyll/powerful-things-markdown-editor/"
#             body = request.get_json()
#             number = body.get("tag")
#             data = {
#                 "tag": number
#             }

#             try:
#                 response = requests.post(endpoint, json=data, headers={'Content-Type': 'application/json'})
#                 if response.status_code == 200:
#                     return response.json()
#                 else:
#                     return {"error": "Request failed"}, response.status_code
#             except Exception:
#                 print(traceback.format_exc())
#                 return {"error": "Internal server error"}, 500
        
#         def get(self):
#             message = "example msg"
#             return message
        
#     api.add_resource(binThing, '/', methods=['GET', 'POST'])


# import requests
# from flask import request
# import traceback
# from flask import Blueprint, jsonify
# from flask_restful import Api, Resource
# from flask_cors import CORS

# binary_api = Blueprint('binary_api', __name__, url_prefix='/api/binary')
# api = Api(binary_api)

# CORS(binary_api, methods=['GET', 'POST'], origins='*')

# class BinaryAPI:
#     class binThing(Resource):
#         def post(self):
#             endpoint = "http://127.0.0.1:4000/mediumish-theme-jekyll/powerful-things-markdown-editor/"
#             body = request.get_json()
#             number = body.get("tag")
#             data = {
#                 "tag": number
#             }

#             try:
#                 response = requests.post(endpoint, json=data, headers={'Content-Type': 'application/json'})
#                 if response.status_code == 200:
#                     return response.json()
#                 else:
#                     return {"error": "Request failed"}, response.status_code
#             except Exception:
#                 print(traceback.format_exc())
#                 return {"error": "Internal server error"}, 500
        
#         def get(self):
#             message = "example msg"
#             return message
        
#     api.add_resource(binThing, '/get', endpoint='get', methods=['GET'])
#     api.add_resource(binThing, '/post', endpoint='post', methods=['POST'])

# @binary_api.after_request
# def after_request(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
#     return response

# API RECEIVING BNARY NUMBER

import requests
from flask import request
import traceback
from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS


import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
import Adafruit_CharLCD as LCD
from multiprocessing import Process




binary_api = Blueprint('binary_api', __name__, url_prefix='/api/binary')
api = Api(binary_api)

CORS(binary_api, methods=['GET', 'POST'], origins='*')

class GetBinary(Resource):
    def get(self):
        message = "example msg"
        return message

class PostBinary(Resource):
    def post(self):
        endpoint = "http://127.0.0.1:4000/mediumish-theme-jekyll/powerful-things-markdown-editor/"
        body = request.get_json()
        number = body.get("tag")
        data = {
            "tag": number
        }
                # Flag variable to track if number has been printed
        flag = False

        try:
            if not flag:
                print("NUMBER:" + number)
                flag = True
        except: 
            print("No Number")
            
        try:
            response = requests.post("http://127.0.0.1:8086/api/binary/post", json=data, headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": "Request failed"}, response.status_code
        except Exception:
            print(traceback.format_exc())
            return {"error": "Internal server error"}, 500
    
    # # API USING BINARY NUMBER

    def matrixAction():
        def main(cascaded, block_orientation, rotate):
        
            # create matrix device
            serial = spi(port=0, device=1, gpio=noop())
            device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
            # debugging purpose
            print("[-] Matrix initialized")

            # print hello world on the matrix display
            msg = number
            # debugging purpose
            print("[-] Printing: %s" % msg)
            show_message(device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)
        if __name__ == "__main__":
        
            try:
                main(cascaded=1, block_orientation=90, rotate=0)
            except KeyboardInterrupt:
                pass
        # cascaded = Number of cascaded MAX7219 LED matrices, default=1
        # block_orientation = choices 0, 90, -90, Corrects block orientation when wired vertically, default=0
        # rotate = choices 0, 1, 2, 3, Rotate display 0=0°, 1=90°, 2=180°, 3=270°, default=0
    





    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    # Example using a character LCD backpack.

    # Define LCD column and row size for 16x2 LCD.
    def lcdAction():
        lcd_columns = 16
        lcd_rows    = 2

        # Initialize the LCD using the pins
        lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

        try:
            # Turn backlight on
            lcd.set_backlight(0)

            # Print a two line message
            lcd.message(number)

        except KeyboardInterrupt:
            # Turn the screen off
            lcd.clear()
            lcd.set_backlight(1)
            

    if __name__=='__main__':
        p2 = Process(target=lcdAction())
        p2.start
        p1 = Process(target=matrixAction())
        p1.start()
        p1.join()
        p2.join()


        
@binary_api.after_request
def after_request(response):
#    response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1:4000")
    response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response



api.add_resource(GetBinary, '/get', endpoint='get')
api.add_resource(PostBinary, '/post', endpoint='post')

