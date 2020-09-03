from base import Session
from models.users import User
from config import SECRET_KEY
import base64



def healthcheck():
    try:
        session = Session()
        print("Session with DB has been opened")
        session.close()
        print("Session with DB has been opened")
        return True
    except:
        print("Error in establishing connection with DB!!")
        session.close()
        return False