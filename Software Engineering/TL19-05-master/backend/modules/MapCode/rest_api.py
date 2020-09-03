from flask import make_response,request
from flask_restplus import Namespace, Resource, fields
import json
from . import lib

NAMESPACE = Namespace('MapCode', description='Get all map codes.')
# app = Flask(__name__)
@NAMESPACE.route('/mapCode/<text>')
class GetMapCode(Resource):
   def get(self, text):

      print(request.url)
      print(text)
      return_dict = lib.get_MapCode(text)

      response = make_response(json.dumps(return_dict))
      response.headers['content-type'] = 'application/test+json'     
      return response