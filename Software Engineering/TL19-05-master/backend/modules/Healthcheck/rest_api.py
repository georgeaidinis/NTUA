from flask import make_response,request
from flask_restplus import Namespace, Resource, fields
import json
import jwt

from base import Session
from . import lib
from config import SECRET_KEY


NAMESPACE = Namespace('', description='Perform a Healthcheck')

@NAMESPACE.route('/Healthcheck')
class Healthcheck(Resource):
    def get(self):
        try:
            return_value = lib.healthcheck()
            print("Return Value = ", return_value)
            if return_value:
                response_text = {"status":"OK"}
                print (response_text)
                response = make_response(json.dumps(response_text))
            else:
                response_text = {"status":"Not OK"}
                print (response_text)
                response = make_response(json.dumps(response_text))
        except:
            response_text = {"status":"Not OK"}
            print (response_text)
            response = make_response(json.dumps(response_text))        
        return response
