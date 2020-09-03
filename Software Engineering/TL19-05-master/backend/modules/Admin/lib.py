from base import Session
from models.users import User
from models.ActualTotalLoad import ActualTotalLoad
from models.AggregatedGenerationPerType import AggregatedGenerationPerType
from models.DayAheadTotalLoadForecast import DayAheadTotalLoadForecast
import jwt
from config import SECRET_KEY
import base64
import pandas as pd

def sign_in(my_username, my_password,my_email,my_quota):
    try:
        session = Session()
        usernames_q = session.query(User).with_entities(User.username)
        print("executing query")
        for username in usernames_q:
            if my_username == username[0]:
                session.close()
                print("returning")
                response = 'Username already taken! Please use another username.'
                return response
        newUser = User(id = None, username = my_username, password = base64.b64encode(my_password.encode('utf-8')),role = 0,daily_quotas = my_quota,current_quotas=my_quota, email = my_email,last_login = None)
        # newUser = User(id, password, username, role, daily_quotas, email,current_quotas,last_login)
        session.add(newUser)
        session.commit()
        print("after commiting")
        response="Signed in successfully!! You can use your new credentials to log in."
        session.close()
        return response
    except:
        print("Error in signing in!!")
        session.close()
        return None
    return response

def showUser(username):
    try:
        session = Session()
        return_dict = {}
        q = session.query(User).with_entities(User.id, User.username, User.password, User.role, User.daily_quotas, User.email, User.last_login, User.current_quotas).filter(User.username == username)
        for user in q:
            print("before")
            return_dict["id"] = user[0]
            return_dict["username"] = user[1]
            return_dict["password"] = user[2]
            return_dict["role"] = user[3]
            return_dict["daily_quotas"] = user[4]
            return_dict["email"] = user[5]
            return_dict["last_login"] = str(user[6])
            return_dict["current_quotas"] = user[7]
        print("after")
        session.close()

    except AttributeError :
        print("Couldn't get user's details")
    except TypeError:
        print("Typerror")
        return None

    return return_dict


def editUser(username, password,email,quota):
    try:
        session = Session()
        return_dict = ""
        q = session.query().with_entities(User.id).filter(User.username == username)
        for users in q:
            existing_user = users[0]
        q = session.query(User).filter_by(id = existing_user).update({"password" : password})
        q = session.query(User).filter_by(id = existing_user).update({"email" : email})
        q = session.query(User).filter_by(id = existing_user).update({"daily_quotas" : quota})
        q = session.query(User).filter_by(id = existing_user).update({"current_quotas" : quota})
        session.commit()
        return_dict = "User updated."

    except:
        print("Error in editing")
        return False
    return return_dict


def get_Users():
    try:
        session = Session()
        return_dict={}
        return_dict['Usernames'] = []    #list used for displaying options for autocomplete dropdown
        # return_dict['dep_id'] = {}      #object to get option's id with O(1)
        q=session.query(User).with_entities(User.username)
        for user in q:
            return_dict['Usernames'].append(user[0])
        session.close()
        return return_dict
    except AttributeError:
        print('Error getting usernames.')
        return None
