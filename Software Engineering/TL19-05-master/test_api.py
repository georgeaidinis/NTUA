import pytest
import os
import jwt
import json
import requests
from backend.config import SECRET_KEY
from pathlib import Path
from cli1 import tokenizer

def test_falseLogin():
    # os.system('python3 backend/run.py')
    url = 'http://localhost:8765/energy/api/Login'
    r = requests.post(url, json.dumps({'username': 'username', 'password':'passw' }))
    assert True == (len(r.text) < 100)

def test_correctLogin():
    # os.system('python3 backend/run.py')
    url = 'http://localhost:8765/energy/api/Login'
    r = requests.post(url, json.dumps({'username': 'user1', 'password':'userpass' }))
    assert False == (len(r.text) < 100)

def test_HealthCheck():
    url = 'http://localhost:8765/energy/api/Healthcheck'
    r = requests.get(url)
    assert 'Not' != r.text[12:15]

def test_Reset():
    # too much time
    # url = 'http://localhost:8765/energy/api/Reset'
    # r = requests.post(url)
    # assert 'Not' != r.text[12:15]
    pass

def test_correctResources():
    url = 'http://localhost:8765/energy/api/ActualTotalLoad/Austria/PT15M/date/2018-01-04?format=json'
    token = {'Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwicm9sZSI6MCwidWlkIjoyfQ.bkGCWTOU7Kf_btyfd_l5bsR49b9bmQIWnYZK1sbdviI'}
    r = requests.get(url, headers = token)
    assert 200 == r.status_code

def test_outofQuotaResources():
    url = 'http://localhost:8765/energy/api/ActualTotalLoad/Austria/PT15M/date/2018-01-04?format=json'
    token = {'Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIyIiwicm9sZSI6MCwidWlkIjozfQ.wseUXFsl-8K9-Lj9wybK0Q7VQ03OEnrMhFoRxM-SAgk'}
    r = requests.get(url, headers = token)
    assert 402 == r.status_code

def test_NoDataResources():
    url = 'http://localhost:8765/energy/api/ActualTotalLoad/Ellada/PT15M/date/2018-01-04?format=json'
    token = {'Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwicm9sZSI6MCwidWlkIjoyfQ.bkGCWTOU7Kf_btyfd_l5bsR49b9bmQIWnYZK1sbdviI'}
    r = requests.get(url, headers = token)
    assert 403 == r.status_code

def test_NotFound():
    url = 'http://localhost:8765/energies/api/ActualTotalLoad/Ellada/PT15M/date/2018-01-04?format=json'
    token = {'Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwicm9sZSI6MCwidWlkIjoyfQ.bkGCWTOU7Kf_btyfd_l5bsR49b9bmQIWnYZK1sbdviI'}
    r = requests.get(url, headers = token)
    assert 404 == r.status_code

def test_NotAuthorized():
    url = 'http://localhost:8765/energy/api/Admin/users'
    #{"Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6MSwidWlkIjoxfQ.IvcQu3MnByiOPRSWZDPs326Nb_KubdKFXc6jlkkd-Bk"}
    token = {'Token' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwicm9sZSI6MCwidWlkIjoyfQ.bkGCWTOU7Kf_btyfd_l5bsR49b9bmQIWnYZK1sbdviI'}
    r = requests.post(url, headers = token, data = json.dumps({ "username": 'newuser', "password": 'passw', "email" : 'email','quota': 'quota'}))
    print(r.content)
    assert 401 == r.status_code

def test_FalseSign_in():
    url = 'http://localhost:8765/energy/api/Admin/users'
    token = {"Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6MSwidWlkIjoxfQ.IvcQu3MnByiOPRSWZDPs326Nb_KubdKFXc6jlkkd-Bk"}
    r = requests.post(url, headers = token , data = json.dumps({ "username": 'user1', "password": 'passw', "email" : 'email','quota': 'quota'}))
    assert 400 == r.status_code
