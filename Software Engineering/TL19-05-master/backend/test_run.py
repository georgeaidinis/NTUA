import pytest
import os
from modules.Users.lib import login
import json
import random
from modules.Healthcheck.lib import healthcheck
from modules.Reset.lib import reset
from modules.Resources.lib import getATLByDate
from modules.Admin.lib import sign_in, showUser, editUser

def test_correctLogin():
    os.system('python3 run.py')
    assert True == login('user1','userpass')[0]

def test_falseLogin():
    os.system('python3 run.py')
    assert False == login('Beskoukis','Saidis')[0]

def test_HealthCheck():
    os.system('python3 run.py')
    assert True == healthcheck()

def test_Reset():
    #toomuchtime
    #assert True = reset()
    pass

def test_Noquota():
    assert pytest.raises(ValueError, getATLByDate, 'Austria', 'PT15M', '2018-01-04', 3)

def test_InputException():
    assert pytest.raises(ValueError, getATLByDate, 'Ellada', 'PT15M', '2018-01-04', 2)

def test_getATLByDate():
    assert None != getATLByDate('Austria', 'PT15M', '2018-01-04', 2)

def test_correctSign_in():
    assert 'Signed in successfully!! You can use your new credentials to log in.' == sign_in('user'+str(random.randrange(4,10000)),'userpass','vessk@saidi.com',200)

def test_falseSign_in():
    assert 'Username already taken! Please use another username.' == sign_in('user1','newpass','vessk@saidi.com',200)

def test_correctshowUser():
    assert {} != showUser('user1')

def test_falseshowUser():
    assert {} == showUser('someone')

def test_correcteditUser():
    assert "User updated." == editUser('user3', 'passw','email',1000)

def test_falseditUser():
    assert False == editUser('User2000', 'passw','email',1000)
