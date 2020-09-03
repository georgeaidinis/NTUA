from flask import make_response,request
from flask_restplus import Namespace, Resource, fields
import json
import jwt

from base import Session
from models.users import User
from . import lib
from config import SECRET_KEY



NAMESPACE = Namespace('', description='Get login attributes.')

LOGIN_MODEL = NAMESPACE.model('login', {
    'username': fields.String(description="user's username", example='admin'),
    'password': fields.String(description="user's password", example='321nimda')
})

@NAMESPACE.route('/Login')
@NAMESPACE.expect(LOGIN_MODEL, validate=True)
# @NAMESPACE.param('username', 'username')
# @NAMESPACE.param('password', 'password')
class Login(Resource):
    def post(self):
        try:
            # args = request.args
            args = request.get_json(force=True)
            print(args)
            # credentials = jwt.decode(args["jwt"], SECRET_KEY)
            #print("#################", credentials)
            username = str(args['username'])
            password = str(args['password'])            
        except AttributeError:
            return make_response('Attributes missing!', 401, {'www-Authenticate': 'Basic realm="Login Required"' })
        try:
            return_dict = lib.login(username, password)
            print("return_dict = ", return_dict)
            if return_dict[0]:
                token = jwt.encode({'username' : return_dict[1]['username'], 'role' : return_dict[1]['role'], 'uid' : return_dict[1]['uid']}, SECRET_KEY)
                response = {'Token': token.decode('utf-8')} #to remove b' for bytes
                print (response)
                response = make_response(json.dumps(response))
            else:
                return return_dict[1]
        except:
            print('Error in login.')
            return False        
        return response

@NAMESPACE.route('/check')
class Check_Login(Resource):
    @NAMESPACE.param('token', 'token')
    def get(self):
        args = request.args
        token = args['token']

        response = lib.decode_auth_token(token)
        response = make_response(json.dumps(response))
        return response

@NAMESPACE.route('/Logout')
class Logout(Resource):
	def post(self):
		try:
			headers = request.headers
			Tokencredentials = jwt.decode(headers["token"], SECRET_KEY)
			uid = str(Tokencredentials['uid'])
			if uid == 'None':
				return make_response('Please Log In again!', 401, {'www-Authenticate': 'Basic realm="Login Required"' })
			else:
				if lib.logout(uid):
					return make_response('', 200 , {'www-Authenticate': 'Basic realm="Login Required"' })
				return make_response('', 400, {'www-Authenticate': 'Basic realm="Login Required"' })


		except AttributeError:
			return make_response('Please Log In again!', 401, {'www-Authenticate': 'Basic realm="Login Required"' })