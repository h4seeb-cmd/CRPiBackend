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

import requests
from flask import request
import traceback
from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

binary_api = Blueprint('binary_api', __name__, url_prefix='/api/binary')
api = Api(binary_api)

CORS(binary_api, methods=['GET', 'POST'], origins='*')

class BinaryAPI:
    class binThing(Resource):
        def post(self):
            endpoint = "http://127.0.0.1:4000/mediumish-theme-jekyll/powerful-things-markdown-editor/"
            body = request.get_json()
            number = body.get("tag")
            data = {
                "tag": number
            }

            try:
                response = requests.post(endpoint, json=data, headers={'Content-Type': 'application/json'})
                if response.status_code == 200:
                    return response.json()
                else:
                    return {"error": "Request failed"}, response.status_code
            except Exception:
                print(traceback.format_exc())
                return {"error": "Internal server error"}, 500
        
        def get(self):
            message = "example msg"
            return message
        
    api.add_resource(binThing, '/', methods=['GET', 'POST'])