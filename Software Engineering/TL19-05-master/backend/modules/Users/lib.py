from base import Session
from models.users import User
import jwt
from config import SECRET_KEY
import base64
from sqlalchemy import Date, cast
from datetime import date




def login(my_username, my_password):
    try:
        session = Session()
        authenticated = False
        user_authentication_q = session.query(User).with_entities(User.username, User.password, User.id, User.role)
        print("out")
        if user_authentication_q != []:
            print("in")
            for user in user_authentication_q:
                if my_username == user[0]:
                    if my_password == base64.b64decode(user[1]).decode('utf-8'):
                        authenticated = True
                        return_dict={'username': user[0], 'uid': user[2], 'role': user[3]}
                        break
                    else:
                        error_text = "Wrong password for user " + str(user[0] + ". Please try again.")
                else:
                    error_text = "User " + str(my_username) + " was not found. Check your username or sign in with a new account."
            session.close()
            if authenticated:
                response = (True, return_dict)
            else:
                response = (False, error_text)
        else:
            response = (False, "No users in the database.")
    except:
        print('Error in login')
        return False
    return response

def logout(uid):
    try:
        session = Session()
        #print("hiiii")
        q = session.query(User).filter(id == uid).update({"last_login" :date.today()})
        #print("hiii")
        session.commit()
        #print("hii")
        session.close()
        #print('hi')
        return True
    except:
        return False

def decode_auth_token(auth_token):
    """
    Validates the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, SECRET_KEY)
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False 
