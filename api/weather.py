import requests
from flask import request
import traceback
from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from api.weatherLCD import lcdOn

weather_api = Blueprint('weather_api', __name__, url_prefix='/api/weather')
api = Api(weather_api)
CORS(weather_api, methods=['GET', 'POST'], origins='*')
class GetWeather(Resource):
    def get(self):
        message = "example msg"
        return message

class PostWeather(Resource):
    def post(self):
        endpoint = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
        body = request.get_json()
        location = body.get("location")
        query_param = body.get("query_param")
        querystring = {query_param: location}
        headers = {
            "X-RapidAPI-Key": "9e76af0f32msh97501ce28ffe3b8p1c0da6jsnc3113faae226",
            "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com",
            'Content-Type': 'application/json'
        }
        try:
            response = requests.get(endpoint, params=querystring, headers=headers)
            if response.status_code == 200:
                return response.json()
                lcdOn(location)
            else:
                return {"error": "Request failed"}, response.status_code
        except Exception:
            print(traceback.format_exc())
            return {"error": "Internal server error"}, 500

# @api.after_request

def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response
api.add_resource(GetWeather, '/get', endpoint='get')
api.add_resource(PostWeather, '/post', endpoint='post')

