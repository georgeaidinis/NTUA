from base import Session
from models.ActualTotalLoad import ActualTotalLoad
from models.AggregatedGenerationPerType import AggregatedGenerationPerType
from models.DayAheadTotalLoadForecast import DayAheadTotalLoadForecast
from models.AreaTypeCode import AreaTypeCode
from models.ResolutionCode import ResolutionCode
from models.MapCode import MapCode
from models.ProductionType import ProductionType
from models.users import User
from sqlalchemy import func, distinct
import datetime



class OutOfQuota(Exception):
   pass

class NoData(Exception):
    pass


def getATLByDate(area, resCodeText, date_interval, uid):
    # print(area, resCodeText, date_interval)
    # print(date_interval.split("-")[0], date_interval.split("-")[1], date_interval.split("-")[2])

    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        q = session.query().with_entities(ActualTotalLoad.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, ActualTotalLoad.Year, ActualTotalLoad.Month, ActualTotalLoad.Day, ActualTotalLoad.DateTime, ActualTotalLoad.TotalLoadValue,  ActualTotalLoad.UpdateTime).\
            filter(ActualTotalLoad.AreaName == area, ActualTotalLoad.AreaTypeCodeId == AreaTypeCode.id, ActualTotalLoad.MapCodeId == MapCode.id, ActualTotalLoad.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, ActualTotalLoad.Year == date_interval.split("-")[0], ActualTotalLoad.Month == date_interval.split("-")[1], ActualTotalLoad.Day == date_interval.split("-")[2])

        q = q.order_by(ActualTotalLoad.DateTime)
        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "ActualTotalLoad"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["Day"] = record[6]
            buffer["DateTimeUTC"] = str(record[7])
            buffer["ActualTotalLoadValue"] = record[8]
            buffer["UpdateTimeUTC"] = str(record[9])
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()

        # for login in q:
        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict


def getATLByMonth(area, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        print("before query")
        q = session.query().with_entities(ActualTotalLoad.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, ActualTotalLoad.Year, ActualTotalLoad.Month, ActualTotalLoad.Day, func.sum(ActualTotalLoad.TotalLoadValue)).\
            filter(ActualTotalLoad.AreaName == area, ActualTotalLoad.AreaTypeCodeId == AreaTypeCode.id, ActualTotalLoad.MapCodeId == MapCode.id, ActualTotalLoad.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, ActualTotalLoad.Year == date_interval.split("-")[0], ActualTotalLoad.Month == date_interval.split("-")[1])

        q = q.group_by(ActualTotalLoad.Day)
        q = q.order_by(ActualTotalLoad.DateTime)
        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "ActualTotalLoad"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["Day"] = record[6]
            buffer["ActualTotalLoadByDayValue"] = record[7]
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()

        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict


def getATLByYear(area, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        q = session.query().with_entities(ActualTotalLoad.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, ActualTotalLoad.Year, ActualTotalLoad.Month, func.sum(ActualTotalLoad.TotalLoadValue)).\
            filter(ActualTotalLoad.AreaName == area, ActualTotalLoad.AreaTypeCodeId == AreaTypeCode.id, ActualTotalLoad.MapCodeId == MapCode.id, ActualTotalLoad.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, ActualTotalLoad.Year == date_interval)

        q = q.group_by(ActualTotalLoad.Month)
        q = q.order_by(ActualTotalLoad.DateTime)
        print(q)
        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "ActualTotalLoad"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["ActualTotalLoadByMonthValue"] = record[6]
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:
            
        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict



def getAGTByDate(area, productionType, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        q = session.query().with_entities(AggregatedGenerationPerType.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, AggregatedGenerationPerType.Year, AggregatedGenerationPerType.Month, AggregatedGenerationPerType.Day, AggregatedGenerationPerType.DateTime, ProductionType.ProductionTypeText, AggregatedGenerationPerType.ActualGenerationOutput, AggregatedGenerationPerType.UpdateTime).\
            filter(AggregatedGenerationPerType.AreaName == area, AggregatedGenerationPerType.ProductionTypeId == ProductionType.id, AggregatedGenerationPerType.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, AggregatedGenerationPerType.AreaTypeCodeId == AreaTypeCode.id, AggregatedGenerationPerType.MapCodeId == MapCode.id, AggregatedGenerationPerType.Year == date_interval.split("-")[0], AggregatedGenerationPerType.Month == date_interval.split("-")[1], AggregatedGenerationPerType.Day == date_interval.split("-")[2])


        if productionType != "AllTypes":
            q = q.filter(ProductionType.ProductionTypeText == productionType)


        q = q.order_by(AggregatedGenerationPerType.DateTime)

        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "AggregatedGenerationPerType"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["Day"] = record[6]
            buffer["DateTimeUTC"] = str(record[7])
            buffer["ProductionType"] = record[8]
            buffer["ActualGenerationOutputValue"] = record[9]
            buffer["UpdateTimeUTC"] = str(record[10])
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict



def getAGTByMonth(area, productionType, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        print("check prod")
        q = session.query().with_entities(AggregatedGenerationPerType.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, AggregatedGenerationPerType.Year, AggregatedGenerationPerType.Month, AggregatedGenerationPerType.Day, ProductionType.ProductionTypeText, func.sum(AggregatedGenerationPerType.ActualGenerationOutput)).\
            filter(AggregatedGenerationPerType.AreaName == area, AggregatedGenerationPerType.ProductionTypeId == ProductionType.id, AggregatedGenerationPerType.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, AggregatedGenerationPerType.AreaTypeCodeId == AreaTypeCode.id, AggregatedGenerationPerType.MapCodeId == MapCode.id, AggregatedGenerationPerType.Year == date_interval.split("-")[0], AggregatedGenerationPerType.Month == date_interval.split("-")[1])

        if productionType != "AllTypes":
            q = q.filter(ProductionType.ProductionTypeText == productionType)


            q = q.group_by(AggregatedGenerationPerType.Day)
            q = q.order_by(AggregatedGenerationPerType.DateTime)

        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "AggregatedGenerationPerType"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["Day"] = record[6]
            buffer["ProductionType"] = record[7]
            buffer["ActualGenerationOutputByDayValue"] = record[8]
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict



def getAGTByYear(area, productionType, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        print("check prod")
        q = session.query().with_entities(AggregatedGenerationPerType.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, AggregatedGenerationPerType.Year, AggregatedGenerationPerType.Month, AggregatedGenerationPerType.Day, ProductionType.ProductionTypeText, func.sum(AggregatedGenerationPerType.ActualGenerationOutput)).\
            filter(AggregatedGenerationPerType.AreaName == area, AggregatedGenerationPerType.ProductionTypeId == ProductionType.id, AggregatedGenerationPerType.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, AggregatedGenerationPerType.AreaTypeCodeId == AreaTypeCode.id, AggregatedGenerationPerType.MapCodeId == MapCode.id, AggregatedGenerationPerType.Year == date_interval)

        if productionType != "AllTypes":
            q = q.filter(ProductionType.ProductionTypeText == productionType)


            q = q.group_by(AggregatedGenerationPerType.Month)
            q = q.order_by(AggregatedGenerationPerType.DateTime)

        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "AggregatedGenerationPerType"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["Day"] = record[6]
            buffer["ProductionType"] = record[7]
            buffer["ActualGenerationOutputByMonthValue"] = record[8]
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict

def getDATLFByDate(area, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        q = session.query().with_entities(DayAheadTotalLoadForecast.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, DayAheadTotalLoadForecast.Year, DayAheadTotalLoadForecast.Month, DayAheadTotalLoadForecast.Day, DayAheadTotalLoadForecast.DateTime, DayAheadTotalLoadForecast.TotalLoadValue,  DayAheadTotalLoadForecast.UpdateTime).\
            filter(DayAheadTotalLoadForecast.AreaName == area, DayAheadTotalLoadForecast.AreaTypeCodeId == AreaTypeCode.id, DayAheadTotalLoadForecast.MapCodeId == MapCode.id, DayAheadTotalLoadForecast.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, DayAheadTotalLoadForecast.Year == date_interval.split("-")[0], DayAheadTotalLoadForecast.Month == date_interval.split("-")[1], DayAheadTotalLoadForecast.Day == date_interval.split("-")[2])

        q =q.order_by(DayAheadTotalLoadForecast.DateTime)

        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "DayAheadTotalLoadForecast"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["Day"] = record[6]
            buffer["DateTimeUTC"] = str(record[7])
            buffer["DayAheadTotalLoadForecastValue"] = record[8]
            buffer["UpdateTimeUTC"] = str(record[9])
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict

def getDATLFByMonth(area, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        print("before query")
        q = session.query().with_entities(DayAheadTotalLoadForecast.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, DayAheadTotalLoadForecast.Year, DayAheadTotalLoadForecast.Month, DayAheadTotalLoadForecast.Day, func.sum(DayAheadTotalLoadForecast.TotalLoadValue)).\
            filter(DayAheadTotalLoadForecast.AreaName == area, DayAheadTotalLoadForecast.AreaTypeCodeId == AreaTypeCode.id, DayAheadTotalLoadForecast.MapCodeId == MapCode.id, DayAheadTotalLoadForecast.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, DayAheadTotalLoadForecast.Year == date_interval.split("-")[0], DayAheadTotalLoadForecast.Month == date_interval.split("-")[1])

        q = q.group_by(DayAheadTotalLoadForecast.Day)
        q = q.order_by(DayAheadTotalLoadForecast.DateTime)
        print(q)
        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "DayAheadTotalLoadForecast"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["Day"] = record[6]
            buffer["DayAheadTotalLoadForecastByDayValue"] = record[7]
            return_dict["records"].append(buffer)


        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict


def getDATLFByYear(area, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        q = session.query().with_entities(DayAheadTotalLoadForecast.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, DayAheadTotalLoadForecast.Year, DayAheadTotalLoadForecast.Month, func.sum(DayAheadTotalLoadForecast.TotalLoadValue)).\
            filter(DayAheadTotalLoadForecast.AreaName == area, DayAheadTotalLoadForecast.AreaTypeCodeId == AreaTypeCode.id, DayAheadTotalLoadForecast.MapCodeId == MapCode.id, DayAheadTotalLoadForecast.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, DayAheadTotalLoadForecast.Year == date_interval)

        q = q.group_by(DayAheadTotalLoadForecast.Month)
        q = q.order_by(DayAheadTotalLoadForecast.DateTime)
        print(q)
        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "DayAheadTotalLoadForecast"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["DayAheadTotalLoadForecastByMonthValue"] = record[6]
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict

def getAvsFByDate(area, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        q = session.query().with_entities(DayAheadTotalLoadForecast.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, DayAheadTotalLoadForecast.Year, DayAheadTotalLoadForecast.Month, DayAheadTotalLoadForecast.Day, DayAheadTotalLoadForecast.DateTime, DayAheadTotalLoadForecast.TotalLoadValue, ActualTotalLoad.TotalLoadValue, DayAheadTotalLoadForecast.UpdateTime).\
            filter(DayAheadTotalLoadForecast.AreaName == area, DayAheadTotalLoadForecast.AreaTypeCodeId == AreaTypeCode.id, DayAheadTotalLoadForecast.MapCodeId == MapCode.id, DayAheadTotalLoadForecast.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, DayAheadTotalLoadForecast.Year == date_interval.split("-")[0], DayAheadTotalLoadForecast.Month == date_interval.split("-")[1], DayAheadTotalLoadForecast.Day == date_interval.split("-")[2]).\
                filter(ActualTotalLoad.AreaName == area, ActualTotalLoad.AreaTypeCodeId == AreaTypeCode.id, ActualTotalLoad.MapCodeId == MapCode.id, ActualTotalLoad.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, ActualTotalLoad.Year == date_interval.split("-")[0], ActualTotalLoad.Month == date_interval.split("-")[1], ActualTotalLoad.Day == date_interval.split("-")[2])

        q =q.order_by(DayAheadTotalLoadForecast.DateTime)

        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "DayAheadTotalLoadForecast"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["Day"] = record[6]
            buffer["DateTimeUTC"] = str(record[7])
            buffer["DayAheadTotalLoadForecastValue"] = record[8]
            buffer["ActualTotalLoadValue"] = record[9]
            buffer["UpdateTimeUTC"] = str(record[10])
            return_dict["records"].append(buffer)


        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict

def getAvsFByMonth(area, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        print("before query")
        q = session.query().with_entities(ActualTotalLoad.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, ActualTotalLoad.Year, ActualTotalLoad.Month, ActualTotalLoad.Day, func.sum(DayAheadTotalLoadForecast.TotalLoadValue), func.sum(ActualTotalLoad.TotalLoadValue)).\
            filter(DayAheadTotalLoadForecast.AreaName == area, DayAheadTotalLoadForecast.AreaTypeCodeId == AreaTypeCode.id, DayAheadTotalLoadForecast.MapCodeId == MapCode.id, DayAheadTotalLoadForecast.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, DayAheadTotalLoadForecast.Year == date_interval.split("-")[0], DayAheadTotalLoadForecast.Month == date_interval.split("-")[1]).\
                filter(ActualTotalLoad.AreaName == area, ActualTotalLoad.AreaTypeCodeId == AreaTypeCode.id, ActualTotalLoad.MapCodeId == MapCode.id, ActualTotalLoad.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, ActualTotalLoad.Year == date_interval.split("-")[0], ActualTotalLoad.Month == date_interval.split("-")[1])

        q = q.group_by(ActualTotalLoad.Day)
        q = q.order_by(ActualTotalLoad.DateTime)
        print(q)
        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "ActualTotalLoad"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["Day"] = record[6]
            buffer["DayAheadTotalLoadForecastByDayValue"] = record[7]
            buffer["ActualTotalLoadByDayValue"] = record[8]
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict

def getAvsFByYear(area, resCodeText, date_interval, uid):
    try:
        session = Session()
        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        #result is in type (id, quota)
        for quota in q:
            if quota[1]==0:
                q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
                for login in q:
                    if login[1]!=datetime.datetime.now().date():
                        q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
                        q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
                #print('User has done too many requests!')
                        if login[2] == 0:
                            session.close()
                            raise OutOfQuota
                    else:
                        session.close()
                        raise OutOfQuota
        session.close()
    except OutOfQuota:
        raise ValueError("Out of Quota")
    except AttributeError:
        raise
    try:
        session = Session()
        q = session.query().with_entities(ActualTotalLoad.AreaName, AreaTypeCode.AreaTypeCodeText, MapCode.MapCodeText, ResolutionCode.ResolutionCodeText, ActualTotalLoad.Year, ActualTotalLoad.Month, func.sum(DayAheadTotalLoadForecast.TotalLoadValue), func.sum(ActualTotalLoad.TotalLoadValue)).\
            filter(DayAheadTotalLoadForecast.AreaName == area, DayAheadTotalLoadForecast.AreaTypeCodeId == AreaTypeCode.id, DayAheadTotalLoadForecast.MapCodeId == MapCode.id, DayAheadTotalLoadForecast.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, DayAheadTotalLoadForecast.Year == date_interval.split("-")[0]).\
                filter(ActualTotalLoad.AreaName == area, ActualTotalLoad.AreaTypeCodeId == AreaTypeCode.id, ActualTotalLoad.MapCodeId == MapCode.id, ActualTotalLoad.ResolutionCodeId == ResolutionCode.id, ResolutionCode.ResolutionCodeText == resCodeText, ActualTotalLoad.Year == date_interval.split("-")[0])

        q = q.group_by(ActualTotalLoad.Month)
        q = q.order_by(ActualTotalLoad.DateTime)
        print(q)
        return_dict = {}
        return_dict["records"] = []
        for record in q:
            buffer = {}
            buffer["Source"] = "entso-e"
            buffer["Dataset"] = "ActualTotalLoad"
            buffer["AreaName"] = record[0]
            buffer["AreaTypeCode"] = record[1]
            buffer["MapCode"] = record[2]
            buffer["ResolutionCode"] = record[3]
            buffer["Year"] = record[4]
            buffer["Month"] = record[5]
            buffer["DayAheadTotalLoadForecastByMonthValue"] = record[6]
            buffer["ActualTotalLoadByMonthValue"] = record[7]
            return_dict["records"].append(buffer)

        # q=session.query().with_entities(User.id, User.last_login, User.daily_quotas).filter(User.id==uid).distinct()
        # for login in q:

        #     if login[1]!=datetime.datetime.now().date():
        #         q = session.query(User).filter_by(id = uid).update({"current_quotas" : login[2]})
        #         q = session.query(User).filter_by(id = uid).update({"last_login" :datetime.datetime.now().date()})
        #     session.commit()
        #     session.close()
        #     session = Session()

        q=session.query().with_entities(User.id, User.current_quotas).filter(User.id==uid).distinct()
        for quota in q:
            existing = quota[1]
        session.close()
        existing -=1

        session = Session()
        q = session.query(User).filter_by(id = uid).update({"current_quotas" :existing})
        session.commit()
        session.close()
        if not record:
            #print(return_dict)
            raise No_data

    except AttributeError:
        raise
    except TypeError:
        raise
    except IndexError:
        raise
    except:
        raise ValueError("No data")
    return return_dict


def get_areas(params):
    try:
        print("in lib")
        dataset = params["dataset"]
        print(dataset)
        mapDatasets = {
            "ActualTotalLoad": ActualTotalLoad,
            "AggregatedGenerationPerType": AggregatedGenerationPerType,
            "DayAheadTotalLoadForecast": DayAheadTotalLoadForecast
        }
        session = Session()
        return_dict={}
        return_dict['Areas'] = []
        if dataset != "ActualvsForecast":
            q=session.query().with_entities(mapDatasets[dataset].AreaName).distinct()
        elif dataset == "ActualvsForecast":
            q = session.query().with_entities(DayAheadTotalLoadForecast.AreaName).distinct()
            sub_q = session.query().with_entities(ActualTotalLoad.AreaName).distinct().subquery()
            q = q.filter(DayAheadTotalLoadForecast.AreaName == sub_q.c.AreaName)
        for area in q:
            return_dict['Areas'].append(area[0])
        session.close()
    except AttributeError:
        return False
    return return_dict

def get_resCodes():
    try:
        session = Session()
        return_dict={}
        return_dict['Resolution Codes'] = []
        q=session.query().with_entities(ResolutionCode.ResolutionCodeText).distinct()
        for code in q:
            return_dict['Resolution Codes'].append(code[0])
        session.close()
        return return_dict
    except AttributeError:
        return False
    return return_dict

def get_types():
    try:
        session = Session()
        return_dict={}
        return_dict['Production Types'] = []
        q=session.query().with_entities(ProductionType.ProductionTypeText).distinct()
        for code in q:
            return_dict['Production Types'].append(code[0])
        session.close()
        return return_dict
    except AttributeError:
        return False
    return return_dict
