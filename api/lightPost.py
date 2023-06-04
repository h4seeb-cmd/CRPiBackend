import requests
from flask import request
import traceback
from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from api.lightTest import LightSensor
import time

light_api = Blueprint('light_api', __name__, url_prefix='/api/light')
api = Api(light_api)

CORS(light_api, methods=['GET'], origins='*')

class GetLight(Resource):
    def get(self):
        sensor = LightSensor()
        try:
            while True:
                return("Light Level : " + str(sensor.readLight()) + " lx")
                time.sleep(10)
        except KeyboardInterrupt:
            pass


api.add_resource(GetLight, '/get', endpoint='get')