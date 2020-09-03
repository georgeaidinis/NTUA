from base import Session
from models.ActualTotalLoad import ActualTotalLoad
from models.AggregatedGenerationPerType import AggregatedGenerationPerType
from models.DayAheadTotalLoadForecast import DayAheadTotalLoadForecast
from models.users import User
from config import SECRET_KEY
import base64




def reset():
    try:
        session = Session()
        print("Session with DB has been opened")

        #delete all rows
        session.query(ActualTotalLoad).delete()
        session.query(AggregatedGenerationPerType).delete()
        session.query(DayAheadTotalLoadForecast).delete()
        session.query(User).filter(User.username!="admin").delete()



        session.commit()
        session.close()
        print("Session with DB has been opened")
        return True
    except:
        print("Error in establishing connection with DB!!")
        session.close()
        return False
