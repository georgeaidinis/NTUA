from base import Session
from models.MapCode import MapCode
from sqlalchemy import func
import datetime


def get_MapCode(text):
    try:
        session = Session()
        return_dict = {}
        return_dict["MapCodes"] = {}
        q = session.query(MapCode).with_entities(MapCode.id, MapCode.EntityCreatedAt, MapCode.EntityModifiedAt, MapCode.MapCodeText, MapCode.MapCodeNote).filter(MapCode.MapCodeText == text)
        for el in q:
            return_dict["MapCodes"][el[0]] = {}
            return_dict["MapCodes"][el[0]]["Created at"] = el[1].strftime("%Y")
            return_dict["MapCodes"][el[0]]["Modified at"] = el[2].strftime("%Y")
            return_dict["MapCodes"][el[0]]["Text"] = el[3]
            return_dict["MapCodes"][el[0]]["Note"] = el[4]
        
        session.close()
        return return_dict
    except:
        print("Error getting MapCodes")
        return None
