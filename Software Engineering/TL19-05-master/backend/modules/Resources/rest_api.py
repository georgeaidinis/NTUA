from flask import make_response,request
from flask_restplus import Namespace, Resource, fields
from . import lib
import json
import io
import csv
import jwt
import os
import pyexcel as pe
from pathlib import Path
from config import SECRET_KEY



NAMESPACE = Namespace('/', description='Get all resources.')
@NAMESPACE.route('/ActualTotalLoad/<area>/<resCodeText>/<date_type>/<date_interval>')
@NAMESPACE.param('format', 'format')
@NAMESPACE.param('uid', 'uid')
class GetActualTotalLoad(Resource):
    def get(self, area, resCodeText, date_type, date_interval):
        args = request.args
        try:
            # get token from header
            try:
                headers = request.headers
                credentials = jwt.decode(headers["Token"], SECRET_KEY)
                uid = str(credentials['uid'])
            except:
                uid = args['uid']
            # get format parameter
            if date_type == "date":
                return_dict = lib.getATLByDate(area, resCodeText, date_interval,uid)
            elif date_type == "month":
                print("inside")
                return_dict = lib.getATLByMonth(area, resCodeText, date_interval,uid)
            elif date_type == "year":
                return_dict = lib.getATLByYear(area, resCodeText, date_interval,uid)
        except AttributeError: 
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except TypeError: 
            return make_response('Wrong Types!', 400, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except IndexError: 
            return make_response('Bad Index!', 401, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        #except NoData: 
        #    return make_response('No Data Found!', 403, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        #except OutOfQuota: 
        #    print("I reached this point!")
        #    return make_response('Out of Quota!', 402, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except ValueError as error:
            if error.args[0]=="Out of Quota":
                return make_response('Out of Quota!', 402, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
            elif error.args[0]=="No data":
                return make_response('No Data Found!', 403, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        
        print("exiting..")
        response = ""
        if args["format"] == "csv":
            home = str(Path.home())
            csv_file = home + "/temp.csv"
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = ["Source","Dataset","AreaName","AreaTypeCode","MapCode","ResolutionCode","Year","Month","Day",'ActualTotalLoadValue', 'DateTimeUTC', "UpdateTimeUTC"])
                writer.writeheader()
                for data in return_dict["records"]:
                    writer.writerow(data)
            si = io.StringIO()
            cw = csv.writer(si)
            with open(csv_file, newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            cw.writerows(data)
            response = make_response(si.getvalue())
            response.headers["Content-Disposition"] = "attachment; filename=" + area +"_" + resCodeText + "_" + date_type + "_" + date_interval +  ".csv"
            response.headers["Content-type"] = "text/csv"
            os.remove(csv_file)
            return response

        elif  args["format"] == "json":
            response = make_response(json.dumps(return_dict))
            response.headers['content-type'] = 'application/test+json'

        print("before returning")
        return response



@NAMESPACE.route('/AggregatedGenerationPerType/<area>/<productionType>/<resCodeText>/<date_type>/<date_interval>')
@NAMESPACE.param('format', 'format')
@NAMESPACE.param('uid', 'uid')
class GetAggregatedGenerationPerType(Resource):
    def get(self, area, productionType, resCodeText, date_type, date_interval):
        args = request.args
        try:
            try:
             # get token from header
                headers = request.headers
                credentials = jwt.decode(headers["Token"], SECRET_KEY)
                uid = str(credentials['uid'])
            except:
                uid = args['uid']
            if date_type == "date":
                return_dict = lib.getAGTByDate(area, productionType, resCodeText, date_interval,uid)
            elif date_type == "month":
                print("inside")
                return_dict = lib.getAGTByMonth(area, productionType, resCodeText, date_interval,uid)
            elif date_type == "year":
                return_dict = lib.getAGTByYear(area, productionType, resCodeText, date_interval,uid)

        except AttributeError: 
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except TypeError: 
            return make_response('Wrong Types!', 400, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except IndexError: 
            return make_response('Bad Index!', 401, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        #except NoData: 
        #    return make_response('No Data Found!', 403, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        #except OutOfQuota: 
        #    print("I reached this point!")
        #    return make_response('Out of Quota!', 402, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except ValueError as error:
            if error.args[0]=="Out of Quota":
                return make_response('Out of Quota!', 402, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
            elif error.args[0]=="No data":
                return make_response('No Data Found!', 403, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        response = ""
        if args["format"] == "csv":
            home = str(Path.home())
            csv_file = home + "/temp.csv"
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = ["Source","Dataset","AreaName","AreaTypeCode","MapCode","ResolutionCode","Year","Month","Day",'DateTimeUTC',"ProductionType","ActualGenerationOutputValue", "UpdateTimeUTC"])
                writer.writeheader()
                for data in return_dict["records"]:
                    writer.writerow(data)
            si = io.StringIO()
            cw = csv.writer(si)
            with open(csv_file, newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            cw.writerows(data)
            response = make_response(si.getvalue())
            response.headers["Content-Disposition"] = "attachment; filename=AggregatedGenerationPerType_" + area +"_" + resCodeText + "_" + date_type + "_" + date_interval +  ".csv"
            response.headers["Content-type"] = "text/csv"
            os.remove(csv_file)
            return response

        elif  args["format"] == "json":
            response = make_response(json.dumps(return_dict))
            response.headers['content-type'] = 'application/test+json'

        print("before returning")
        return response


@NAMESPACE.route('/DayAheadTotalLoadForecast/<area>/<resCodeText>/<date_type>/<date_interval>')
@NAMESPACE.param('format', 'format')
@NAMESPACE.param('uid', 'uid')
class GetDayAheadTotalLoadForecast(Resource):
    def get(self, area, resCodeText, date_type, date_interval):
        args = request.args
        try:
            try:

                headers = request.headers
                credentials = jwt.decode(headers["Token"], SECRET_KEY)
                uid = str(credentials['uid'])
            except:
                uid = args['uid']
            if date_type == "date":
                return_dict = lib.getDATLFByDate(area, resCodeText, date_interval,uid)
            elif date_type == "month":
                print("inside")
                return_dict = lib.getDATLFByMonth(area, resCodeText, date_interval,uid)
            elif date_type == "year":
                return_dict = lib.getDATLFByYear(area, resCodeText, date_interval,uid)

        except AttributeError: 
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except TypeError: 
            return make_response('Wrong Types!', 400, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except IndexError: 
            return make_response('Bad Index!', 401, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        #except NoData: 
        #    return make_response('No Data Found!', 403, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        #except OutOfQuota: 
        #    print("I reached this point!")
        #    return make_response('Out of Quota!', 402, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except ValueError as error:
            if error.args[0]=="Out of Quota":
                return make_response('Out of Quota!', 402, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
            elif error.args[0]=="No data":
                return make_response('No Data Found!', 403, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        response = ""

        if args["format"] == "csv":
            home = str(Path.home())
            csv_file = home + "/temp.csv"
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = ["Source","Dataset","AreaName","AreaTypeCode","MapCode","ResolutionCode","Year","Month","Day","DateTimeUTC","DayAheadTotalLoadForecastValue","ActualTotalLoadValue","UpdateTimeUTC"])
                writer.writeheader()
                for data in return_dict["records"]:
                    writer.writerow(data)
            si = io.StringIO()
            cw = csv.writer(si)
            with open(csv_file, newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            cw.writerows(data)
            response = make_response(si.getvalue())
            response.headers["Content-Disposition"] = "attachment; filename=DayAheadTotalLoadForecast_" + area +"_" + resCodeText + "_" + date_type + "_" + date_interval +  ".csv"
            response.headers["Content-type"] = "text/csv"
            os.remove(csv_file)
            return response

        elif  args["format"] == "json":
            response = make_response(json.dumps(return_dict))
            response.headers['content-type'] = 'application/test+json'

        print("before returning")
        return response



@NAMESPACE.route('/ActualvsForecast/<area>/<resCodeText>/<date_type>/<date_interval>')
@NAMESPACE.param('format', 'format')
@NAMESPACE.param('uid', 'uid')
class GetActualvsForecast(Resource):
    def get(self, area, resCodeText, date_type, date_interval):
        args = request.args
        try:
            try:
                headers = request.headers
                credentials = jwt.decode(headers["Token"], SECRET_KEY)
                uid = str(credentials['uid'])
            except:
                uid = args['uid']
            if date_type == "date":
                return_dict = lib.getAvsFByDate(area, resCodeText, date_interval,uid)
            elif date_type == "month":
                print("inside")
                return_dict = lib.getAvsFByMonth(area, resCodeText, date_interval,uid)
            elif date_type == "year":
                return_dict = lib.getAvsFByYear(area, resCodeText, date_interval,uid)

        except AttributeError: 
            return make_response('Attributes missing!', 400, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except TypeError: 
            return make_response('Wrong Types!', 400, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except IndexError: 
            return make_response('Bad Index!', 401, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        #except NoData: 
        #    return make_response('No Data Found!', 403, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        #except OutOfQuota: 
        #    print("I reached this point!")
        #    return make_response('Out of Quota!', 402, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        except ValueError as error:
            if error.args[0]=="Out of Quota":
                return make_response('Out of Quota!', 402, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
            elif error.args[0]=="No data":
                return make_response('No Data Found!', 403, {'www-Authenticate': 'Basic realm="Bad Attributes"' })
        response = ""

        if args["format"] == "csv":
            home = str(Path.home())
            csv_file = home + "/temp.csv"
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = ["Source","Dataset","AreaName","AreaTypeCode","MapCode","ResolutionCode","Year","Month","Day","DateTimeUTC","DayAheadTotalLoadForecastValue","ActualTotalLoadValue","UpdateTimeUTC"])
                writer.writeheader()
                for data in return_dict["records"]:
                    writer.writerow(data)
            si = io.StringIO()
            cw = csv.writer(si)
            with open(csv_file, newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            cw.writerows(data)
            response = make_response(si.getvalue())
            response.headers["Content-Disposition"] = "attachment; filename=ActualvsForecast_" + area +"_" + resCodeText + "_" + date_type + "_" + date_interval +  ".csv"
            response.headers["Content-type"] = "text/csv"
            os.remove(csv_file)
            return response

        elif  args["format"] == "json":
            response = make_response(json.dumps(return_dict))
            response.headers['content-type'] = 'application/test+json'

        print("before returning")
        return response

@NAMESPACE.route('/get_areas')
@NAMESPACE.param('dataset', 'dataset')
class getAreaNames(Resource):
    def get(self):
        # try:
        args = request.args
        return_dict = lib.get_areas(args)
        response = make_response(json.dumps(return_dict))
        response.headers['content-type'] = 'application/ElectroMarket+json'
        # except:
            # print("Error getting areas!")
            # return False
        return response

@NAMESPACE.route('/get_resCodes')
class getResCodes(Resource):
    def get(self):
        # try:
        return_dict = lib.get_resCodes()
        response = make_response(json.dumps(return_dict))
        response.headers['content-type'] = 'application/test+json'
        # except:
        #     print("Error getting Resolution Codes!")
            # return False
        return response

@NAMESPACE.route('/get_types')
class getTypes(Resource):
    def get(self):
        # try:
        return_dict = lib.get_types()
        response = make_response(json.dumps(return_dict))
        response.headers['content-type'] = 'application/test+json'
        # except:
            # print("Error getting Production Types!")
            # return False
        return response
