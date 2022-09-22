import requests
import time
from httpTest.likeui.Common.util import md5,logHttpRst,writeJson,readJson
from httpTest.likeui.mylog import log
from httpTest.likeui.conftest import TEST_HOST_3,is_Not_Run,Run_Reason
from httpTest.likeui.DataHelp.Data_User import DataUser
import base64
import allure
import pytest

@allure.step
@logHttpRst
def testo1():
    rsp = requests.get('%s/api/private/v1/categories'%TEST_HOST_3),
    return rsp


'''
@allure.step
@logHttpRst
def register(name, phone, username, email, password):
    rsp = requests.post('%s/user/register'%TEST_HOST_3,
                      data={'name': name, 'phone': phone, 'addr': 'ttt', 'username': username,
                            'email': email, 'password': password, 'code': '1111', 'is_mt': 0})

    return rsp
'''

