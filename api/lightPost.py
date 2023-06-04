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
        light_level = sensor.readLight()
        return(jsonify({"Light_Level": light_level}))


api.add_resource(GetLight, '/get', endpoint='get')