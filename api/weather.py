import requests
from flask import request
import traceback
from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
weather_api = Blueprint('weather_api', __name__, url_prefix='/api/weather')
api = Api(weather_api)
CORS(weather_api, methods=['GET', 'POST'], origins='*')
class GetWeather(Resource):
    def get(self):
        message = "example msg"
        return message
