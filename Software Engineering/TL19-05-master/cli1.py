from cmd import Cmd
import six
import pyfiglet
import urllib3
import requests
import click
from datetime import date
import csv
import os
import json
import jwt
from pathlib import Path
from backend.config import SECRET_KEY


def tokenizer(filename):
    if os.path.exists(filename):
        filereader = open(filename, 'r')
        Data = filereader.readline()
        filereader.close()
        token = str(Data[11:len(Data)-2])
        return {"Token":token}
    else:
        click.echo("You need to login for this action")
        return None

def errorhandling(r):
    if r.status_code == 400:
        click.echo(str(r.status_code)+ ": Bad request")
        return False
    elif r.status_code == 401:
        click.echo(str(r.status_code)+ ": Not authorized")
        return False
    elif r.status_code == 402:
        click.echo(str(r.status_code)+ ": Out of quota")
        return False
    elif r.status_code == 403:
        click.echo(str(r.status_code)+ ": No data")
        return False
    elif r.status_code == 404:
        click.echo(str(r.status_code)+ ": Not Found")
        return False
    elif r.status_code == 200:
        return True
    else:
        click.echo("Other status code: "+ str(r.status_code))
        return False


def dateresolver(date):
    if len(date) == 10:
        return "date/" + date
    elif len(date) == 7:
        return "month/" + date
    elif len(date) == 4:
        return "year/" + date
    return ""

home = str(Path.home())
base_url = "http://localhost:8765/energy/api"
def log(string):
    print(pyfiglet.figlet_format(string))

@click.group()
def cli1():
    pass

@click.group()
def cli2():
    pass
@click.group()
def cli3():
    pass

@click.option('--format', type=click.Choice(['csv', 'json']), default='json' , help='The format with which you want the results to be in')
@cli1.command()
def Healthcheck(format):
    url = base_url + "/Healthcheck"
    newfile = home + "/Healthcheck" + '.' + format
    r = requests.get(url)
    if errorhandling(r):
        with open(newfile, 'w') as new:
                if format == 'json':
                    json.dump(r.json(), new)
                else:
                    new.write(r.content.decode("UTF-8"))
        click.echo("Healtchek data downloaded at " + newfile)




@click.option('--format', type=click.Choice(['csv', 'json']), default='json' , help='The format with which you want the results to be in')
@cli1.command()
def Reset(format):
    url = base_url + "/Reset"
    newfile = home + "/Reset" + '.' + format
    r = requests.post(url)
    if errorhandling(r):
        with open(newfile, 'w') as new:
                if format == 'json':
                    json.dump(r.json(), new)
                else:
                    new.write(r.content.decode("UTF-8"))
        click.echo("Reset data downloaded at " + newfile)


@click.option('--passw', prompt='Your password',hide_input=True, help='The password of the User')
@click.option('--username', prompt='Your username', help='The username of the User')
@cli1.command()
def login(username, passw):
    url = base_url + "/Login"
    filename = home + "/softeng19bAPI.token"
    r = requests.post(url, json.dumps({'username': username, 'password':passw }))
    if errorhandling(r):
        if len(r.text)<100:
            click.echo(r.text)
        else:
            file = open(filename, 'w')
            file.write(r.text)
            file.close()
            log("48HourProject")
            log("Welcome to ElectroMarket CLI app!")
            click.echo('Hello %s!' % username)



@cli2.command()
def logout():
    url = base_url + "/Logout"
    filename = home + "/softeng19bAPI.token"
    token = tokenizer(filename)
    if token != None:
        r = requests.post(url, headers=token)
        if errorhandling(r):
            os.remove(filename)
            click.echo('You have logged out. Goodbye!')


@click.option('--format', type=click.Choice(['csv', 'json']), default='json' , help='The format with which you want the results to be in')
@click.option('--date', prompt='Please enter the date', help='Date in YYYY-MM-DD format, Month in YYYY-MM format or Year in YYYY format')
@click.option('--timeres', type=click.Choice(['PT15M', 'PT30M','PT60M']), prompt='Please enter the Time Resolution', help='Can either be PT15M, PT30M or PT60M')
@click.option('--area', prompt='Please enter the area name', help='Name of the Area')
@cli2.command()
def ActualTotalLoad(area, timeres, date, format):
    url = base_url + "/ActualTotalLoad/" + area + "/" + timeres + "/" + dateresolver(date) + '?format=' + format
    filename = home + "/softeng19bAPI.token"
    newfile = home + "/ActualTotalLoad_" + area + "_" + timeres + "_" + dateresolver(date).replace('/','_') + '.' + format
    token = tokenizer(filename)
    #print(token)
    if token!=None:
        r = requests.get(url, headers = token)
        if errorhandling(r):
            with open(newfile, 'w') as new:
                if format == 'json':
                    json.dump(r.json(), new)
                else:
                    new.write(r.content.decode("UTF-8"))
            click.echo("Data downloaded at " + newfile)


@click.option('--format', type=click.Choice(['csv', 'json']), default='json' , help='The format with which you want the results to be in')
@click.option('--date',  prompt='Please enter the date', help='Date in YYYY-MM-DD format, Month in YYYY-MM format or Year in YYYY format')
@click.option('--productiontype', default='AllTypes', help='Enter production type, Default is Alltypes')
@click.option('--timeres', type=click.Choice(['PT15M', 'PT30M','PT60M']), prompt='Please enter the Time Resolution', help='Can either be PT15M, PT30M or PT60M')
@click.option('--area', prompt='Please enter the area name', help='Name of the Area')
@cli2.command()
def AggregatedGenerationPerType(area, timeres, date, productiontype, format):
    url = base_url + "/AggregatedGenerationPerType/" + area + "/" + productiontype + "/" + timeres + "/" + dateresolver(date) + '?format=' + format
    filename = home + "/softeng19bAPI.token"
    newfile = home + "/AggregatedGenerationPerType_" + area + "_" + productiontype + "_" + timeres + "_" + dateresolver(date).replace('/','_') + '.' + format
    token = tokenizer(filename)
    if token!=None:
        r = requests.get(url, headers = token)
        if errorhandling(r):
            with open(newfile, 'w') as new:
                if format == 'json':
                    json.dump(r.json(), new)
                else:
                    new.write(r.content.decode("UTF-8"))
            click.echo("Data downloaded at " + newfile)



@click.option('--format', type=click.Choice(['csv', 'json']), default='json' , help='The format with which you want the results to be in')
@click.option('--date', default=str(date.today()), prompt='Please enter the date', help='Date in YYYY-MM-DD format, Month in YYYY-MM format or Year in YYYY format')
@click.option('--timeres', type=click.Choice(['PT15M', 'PT30M','PT60M']), prompt='Please enter the Time Resolution', help='Can either be PT15M, PT30M or PT60M')
@click.option('--area', prompt='Please enter the area name', help='Name of the Area')
@cli2.command()
def DayAheadTotalLoadForecast(area, timeres, date, format):
    url = base_url + "/DayAheadTotalLoadForecast/" + area + "/" + timeres + "/" + dateresolver(date) + '?format=' + format
    filename = home + "/softeng19bAPI.token"
    newfile = home + "/DayAheadTotalLoadForecast_" + area + "_" + timeres + "_" + dateresolver(date).replace('/','_') + '.' + format
    token = tokenizer(filename)
    if token!=None:
        r = requests.get(url, headers = token)
        if errorhandling(r):
            with open(newfile, 'w') as new:
                if format == 'json':
                    json.dump(r.json(), new)
                else:
                    new.write(r.content.decode("UTF-8"))
            click.echo("Data downloaded at " + newfile)


@click.option('--format', type=click.Choice(['csv', 'json']), default='json' , help='The format with which you want the results to be in')
@click.option('--date', default=str(date.today()), prompt='Please enter the date', help='Date in YYYY-MM-DD format, Month in YYYY-MM format or Year in YYYY format')
@click.option('--timeres', type=click.Choice(['PT15M', 'PT30M','PT60M']), prompt='Please enter the Time Resolution', help='Can either be PT15M, PT30M or PT60M')
@click.option('--area', prompt='Please enter the area name', help='Name of the Area')
@cli2.command()
def ActualvsForecast(area, timeres, date, format):
    url = base_url + "/ActualvsForecast/" + area + "/" + timeres + "/" + dateresolver(date) + '?format=' + format
    filename = home + "/softeng19bAPI.token"
    newfile = home + "/ActualvsForecast_" + area + "_" + timeres + "_" + dateresolver(date).replace('/','_') + '.' + format
    token = tokenizer(filename)
    if token!=None:
        r = requests.get(url, headers = token)
        if errorhandling(r):
            with open(newfile, 'w') as new:
                if format == 'json':
                    json.dump(r.json(), new)
                else:
                    new.write(r.content.decode("UTF-8"))
            click.echo("Data downloaded at " + newfile)


@click.option('--format', type=click.Choice(['csv', 'json']), default='json' , help='The format with which you want the results to be in')
@click.option('--source', help='Filename')
@click.option('--newdata', default=None, help='Adds data to one of the ActualTotalLoad, AggregatedGenerationPerType, DayAheadTotalLoadForecast tables')
@click.option('--userstatus', default=None, help="Returns the status of the selected user")
@click.option('--quota', help='24hour limit quota')
@click.option('--email', help="The user's email address")
@click.option('--passw', help='The password of the User')
@click.option('--newuser', default=None, help="User's username")
@click.option('--moduser', default=None, help="User's username")

@cli3.command()
def Admin(newuser,moduser,passw,email,quota,userstatus,newdata,source,format):
    url = base_url + "/Admin/"
    filename = home + "/softeng19bAPI.token"
    sum = 0
    for i in [newuser,moduser,userstatus,newdata]:
        if i != None:
            sum += 1

    if  sum != 1 :
        click.echo("You need to select only one of the --newuser, --moduser, --userstatus, --newdata")
        return

    filename = home + "/softeng19bAPI.token"
    token = tokenizer(filename)
    if token != None:
        if newuser != None:
            url = url + 'users'
            myjson = {}
            myjson["username"] = newuser
            myjson["password"] = passw
            myjson["email"] = email
            myjson["quota"] = quota
            r = requests.post(url, headers = token, data = json.dumps(myjson))
            if errorhandling(r):
                click.echo("The new user has been added successfully")

        elif moduser != None:
            url = url + 'users/' + moduser
            myjson = {}
            myjson["password"] = passw
            myjson["email"] = email
            myjson["quota"] = quota
            r = requests.put(url, headers = token, data = json.dumps(myjson))
            if errorhandling(r):
                click.echo("The user has been modified successfully")

        elif userstatus != None:
            url = url + 'users/' + userstatus
            r = requests.get(url, headers = token)
            print(r)
            if errorhandling(r):
                click.echo(r.content)
                click.echo("Thats all FOLKS")

        elif newdata != None:
            url = url + newdata
            if os.path.exists(source):
                files = {'file': ('source', open(source, 'r'))}
                r = requests.post(url, files = files)
                if errorhandling(r):
                    parsed = json.loads(r.json())
                    print(json.dumps(parsed, indent=2, sort_keys=True))
                    click.echo("Successfully uploaded data")
            else:
                click.echo("You need to provide a source file")

cli = click.CommandCollection(sources=[cli1, cli2, cli3])

if __name__ == '__main__':
    cli()
