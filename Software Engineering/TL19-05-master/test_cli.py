import pytest
import os
import io
from cli1 import tokenizer

def test_login():

    a = os.popen('python3 cli1.py login --username user1 --passw userpass','r').read()
    assert a!= False

def test_badlogin():
    a = os.popen('python3 cli1.py login --username user3 --passw us312erpass','r').read()
    assert len(a) <= 100

def test_HealthCheck():
    a = os.popen('python3 cli1.py healthcheck','r')
    data = a.read()
    assert  'Healtchek data downloaded at /home/theodor/Healthcheck.json' in data

def test_Logout():
    os.system('python3 cli1.py login --username user1 --passw userpass')
    a = os.popen('python3 cli1.py logout','r').read()
    assert 'You have logged out. Goodbye!' in a

def test_Resources():
    os.system('python3 cli1.py login --username user1 --passw userpass')
    a = os.popen('python3 cli1.py actualtotalload --area Austria --timeres PT15M --date 2018-01-04 --format json','r').read()
    assert 'Data downloaded' in a

def test_WrongResources():
    os.system('python3 cli1.py login --username user1 --passw userpass')
    a = os.popen('python3 cli1.py actualtotalload --area Austria --timeres PT15M --date 2020-01-04 --format json','r').read()
    assert '403: No data' in a

def test_OutOfQuota():
    os.system('python3 cli1.py login --username user2 --passw userpass')
    a = os.popen('python3 cli1.py actualtotalload --area Austria --timeres PT15M --date 2018-01-04 --format json','r').read()
    assert '402: Out of quota' in a

def test_AdminViewstatus():
    os.system('python3 cli1.py login --username admin --passw 321nimda')
    a = os.popen('python3 cli1.py admin --userstatus user1','r').read()
    assert '"id"' in a

def test_Adminewusermoduser():
    os.system('python3 cli1.py login --username admin --passw 321nimda')
    os.system('python3 cli1.py admin --newuser some --passw pass --email sad --quota 5')
    os.system('python3 cli1.py admin --moduser some --passw newpass --email sader --quota 50')
    a = os.popen('python3 cli1.py admin --userstatus some','r').read()
    assert '"sader"' in a
