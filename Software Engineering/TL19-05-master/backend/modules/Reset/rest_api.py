from flask import make_response,request
from flask_restplus import Namespace, Resource, fields
import json
import jwt

from base import Session
from . import lib
from config import SECRET_KEY

NAMESPACE = Namespace('', description='Reset the DB')

@NAMESPACE.route('/Reset')
class Reset(Resource):
    def post(self):
        try:
            return_value = lib.reset()
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


