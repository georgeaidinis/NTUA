from flask import make_response,request
from flask_restplus import Namespace, Resource, fields
import json
import jwt
import pandas as pd
from base import Session
from models.users import User
from . import lib
from config import SECRET_KEY
import os
from base import Session
from models.users import User
from models.ActualTotalLoad import ActualTotalLoad
from models.AggregatedGenerationPerType import AggregatedGenerationPerType
from models.DayAheadTotalLoadForecast import DayAheadTotalLoadForecast




NAMESPACE = Namespace('Admin', description='Get login attributes.')


USER_MODEL = NAMESPACE.model('user', {
    'username': fields.String(description="User's username", example="user1"),
    'password': fields.String(description="User's password", example='userpass'),
    'role': fields.Integer(description="User's role", example=1),
    'daily_quotas': fields.Integer(description="Daily quotas", example=1000),
    'email': fields.String(description="User's email", example="user1@48hProjects.com"),
    'login_date': fields.Date(description="User's last login", example="2018-01-01"),
    'current_quotas': fields.Integer(description="Quotas left.", example=500)
})



@NAMESPACE.route("/users")
class Signin(Resource):
    @NAMESPACE.param('jwt', 'Credentials')
    def post(self):
        try:
            credentials = request.get_json(force=True)
            try:

                headers = request.headers
                Tokencredentials = jwt.decode(headers["Token"], SECRET_KEY)
                if Tokencredentials['role']==0:
                    return make_response('You are not an admin', 401)
            except:
                if credentials['role']==0:
                        return make_response('You are not an admin', 401)
            
            username = str(credentials["new_user"]['username'])
            password = str(credentials["new_user"]['password'])
            email = str(credentials["new_user"]['email'])
            quota = str(credentials["new_user"]['quota'])
            if username == 'None' or password == 'None':
                return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
        except AttributeError:
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
        try:
            response = lib.sign_in(username, password, email, quota)
            if response == 'Username already taken! Please use another username.':
                return make_response('Username already taken! Please use another username.',400)
        except:
            print('Error in signing in.')
            return False
        print("success")
        return response

@NAMESPACE.route("/users/<username>")
@NAMESPACE.param("uid", "uid")
class show_editUser(Resource):
    def get(self, username):
        try:
            headers = request.headers
            Tokencredentials = jwt.decode(headers["Token"], SECRET_KEY)
            if Tokencredentials['role']==0:
                return make_response('You are not an admin', 401)
        except:
            args = request.args
            if args["role"] == 0:
                return make_response('You are not an admin', 401)
        return_dict = lib.showUser(username)
        if return_dict == None:
            make_response('Not existing user', 400)
        return return_dict

    def put(self, username):
        try:
            credentials = request.get_json(force= True)
            try:
                headers = request.headers
            # print(password,email,quota)
                Tokencredentials = jwt.decode(headers["Token"], SECRET_KEY)
                if Tokencredentials['role']==0:
                    return make_response('You are not an admin', 401)
            except:
                if credentials['role']==0:
                    return make_response('You are not an admin', 401)
            password = str(credentials['password'])
            email = str(credentials['email'])
            quota = str(credentials['quota'])
            if email == 'None' or password == 'None' or quota == 'None':
                return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
            return_dict = lib.editUser(username, password,email,quota)
        except:
            print("Error editing user.")
            return False
        return return_dict

    def put(self, username):
        try:
            headers = request.headers
            # print(password,email,quota)
            Tokencredentials = jwt.decode(headers["Token"], SECRET_KEY)
            if Tokencredentials['role']==0:
                return make_response('You are not an admin', 401)
            credentials = request.get_json(force= True)
            password = str(credentials['password'])
            email = str(credentials['email'])
            quota = str(credentials['quota'])
            if email == 'None' or password == 'None' or quota == 'None':
                return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
            return_dict = lib.editUser(username, password,email,quota)
        except:
            print("Error editing user.")
            return False
        return return_dict
@NAMESPACE.route('/ActualTotalLoad')
class New_dataATL(Resource):
    def post(self):
        response_text = {}
        try:
            files = request.files
            session = Session()
            total_records_initial = session.query(ActualTotalLoad).count()
            session.close()
            file_obj = files['file']
            data_df = pd.read_csv(file_obj, sep=';')
            data_df.to_csv(r'My_file.csv')
            os.system("mysql -u root -p" + DB_PASS+" < insertATL.sql")
            #print(data_df)
        except AttributeError:
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
        try:
            session = Session()
            records_in_file = 0
            for _, row in data_df.iterrows():
                records_in_file += 1

            total_records = session.query(ActualTotalLoad).count()
            session.close()
            response_text["totalRecordsInFile"] = str(records_in_file)
            response_text["totalRecordsImported"] = str(total_records - total_records_initial)
            response_text["totalRecordsInDatabase"] = str(total_records)

        except:
            print('Error in uploading files.')
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
        print("success")
        if not response_text:
            return make_response('No data!', 403, {'www-Authenticate': 'Basic realm="Login Required"' })
        response = make_response(json.dumps(response_text))
        return response

@NAMESPACE.route('/AggregatedGenerationPerType')
class New_dataAGPT(Resource):
    def post(self):
        response_text = {}
        try:
            files = request.files
            session = Session()
            total_records_initial = session.query(AggregatedGenerationPerType).count()
            session.close()
            file_obj = files['file']
            data_df = pd.read_csv(file_obj, sep=';')
            data_df.to_csv(r'My_file.csv')
            os.system("mysql -u root -p" + DB_PASS+" < insertAGPT.sql")
            #print(data_df)
        except AttributeError:
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
        try:
            session = Session()
            records_in_file = 0
            for _, row in data_df.iterrows():
                records_in_file += 1

            total_records = session.query(AggregatedGenerationPerType).count()
            session.close()
            response_text["totalRecordsInFile"] = str(records_in_file)
            response_text["totalRecordsImported"] = str(total_records - total_records_initial)
            response_text["totalRecordsInDatabase"] = str(total_records)

        except:
            print('Error in uploading files.')
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
        print("success")
        if not response_text:
            return make_response('No data!', 403, {'www-Authenticate': 'Basic realm="Login Required"' })
        response = make_response(json.dumps(response_text))
        return response

@NAMESPACE.route('/DayAheadTotalLoadForecast')
class New_dataDATLF(Resource):
    def post(self):
        response_text = {}
        try:
            files = request.files
            session = Session()
            total_records_initial = session.query(DayAheadTotalLoadForecast).count()
            session.close()
            file_obj = files['file']
            data_df = pd.read_csv(file_obj, sep=';')
            data_df.to_csv(r'My_file.csv')
            os.system("mysql -u root -p" + DB_PASS+" < insertDATLF.sql")
            #print(data_df)
        except AttributeError:
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
        try:
            session = Session()
            records_in_file = 0
            for _, row in data_df.iterrows():
                records_in_file += 1

            total_records = session.query(DayAheadTotalLoadForecast).count()
            session.close()
            response_text["totalRecordsInFile"] = str(records_in_file)
            response_text["totalRecordsImported"] = str(total_records - total_records_initial)
            response_text["totalRecordsInDatabase"] = str(total_records)

        except:
            print('Error in uploading files.')
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Login Required"' })
        print("success")
        if not response_text:
            return make_response('No data!', 403, {'www-Authenticate': 'Basic realm="Login Required"' })
        response = make_response(json.dumps(response_text))
        return response
@NAMESPACE.route('/getUsers')
class GetDepartments(Resource):
    def get(self):
        return_dict = lib.get_Users()
        response = make_response(json.dumps(return_dict))
        response.headers['content-type'] = 'application/nokia.Sophia-Tool+json'
        return response