import requests
import time
from httpTest.likeui.Common.util import md5,logHttpRst,writeJson,readJson
from httpTest.likeui.mylog import log
from httpTest.likeui.conftest import TEST_HOST,TEST_HOST_2,is_Not_Run,Run_Reason
from httpTest.likeui.DataHelp.Data_User import DataUser
import base64
import allure
import pytest


@allure.step
@logHttpRst
def register(name, phone, username, email, password):
    r = requests.post('%s/user/register'%TEST_HOST,
                      data={'name': name, 'phone': phone, 'addr': 'ttt', 'username': username,
                            'email': email, 'password': password, 'code': '1111', 'is_mt': 0})

    return r
@allure.step
@logHttpRst
def login(usr,pwd,code):
    """ 登录请求 ，将响应对象返回"""
    rsp = requests.post('%s/user/login'%TEST_HOST,
                        data = {'email': usr, 'password': pwd, 'code': code, 'is_mt': 0,'isJson':1})
    return rsp

@allure.step
@logHttpRst
def login_sign(email,pwd):
    #当前时间- 1979-1-1 00:00:00 的秒数
    str_time = str(int(time.time()) * 1000)
    sign = md5(str_time + pwd)
    rsp = requests.post('%s/user/login/sign'%TEST_HOST,
                        json={'email': email, 'password': pwd, 'time': str_time, 'sign': sign,'isJson':1})
    return rsp

@allure.step
@logHttpRst
def changeImage(filePath):
    url = "%s/user/changePersonImage"%TEST_HOST
    with open(filePath,'rb') as f:
        ctn = f.read()
        bf = base64.b64encode(ctn)
    #上传datas时，需要的是一个字符串
    rsp = requests.put(url,json={"uid":"0058ff40b88511eb98e900163e0cc54c",'datas':str(bf)})
    log.info(filePath)
    return rsp
#1.register常见的请求
#2.login_sign，签名算法是怎样处理的。
#3.A接口返回的值里面，需要传给B接口。

@allure.step
@logHttpRst
def login_zhiguyichuan(usr,pwd):
    #在登录之前，先读json文件，读完之后存储的是一个DICT
    dict = readJson('../MidTokenVar.json')
    ctn = {"userName": usr, "passWord": pwd}
    rsp = requests.post("%s/login"%TEST_HOST_2, json=ctn)
    #如果请求获取到了openID或者token值，然后我们再写进json文件中
    #如果我们需要这个dict中的key的时候，我们去获取就可以了。
    dict['openId'] = rsp.json().get('data').get('openId')
    dict['token'] = rsp.json().get('data').get('token')
    writeJson('../MidTokenVar.json',dict)
    return rsp
@allure.step
@logHttpRst
def openId_index(openId,token):
    url = "%s/index?token=%s&openId=%s&winWidth=1190&winHeight=734"%(TEST_HOST_2,openId,token)
    rsp = requests.get(url)
    return rsp
@allure.step
@logHttpRst
def totalHtml(openId,token):
    url = "%s/totalHtml?token=%s&openId=%s" % (TEST_HOST_2,openId,token)
    rsp = requests.get(url)
    return rsp

#pip install pytest-ordering 用来控制执行代码的顺序
@allure.step
@pytest.mark.parametrize('usr,pwd',[('qwen','q123456'),('qwen','q123456')])
@pytest.mark.run(order = 0) #设置测试案例执行的顺序。0最先开始的。
@pytest.mark.skipif(is_Not_Run,reason=Run_Reason)
def test_login_success(usr,pwd):
    rsp = login_zhiguyichuan(usr,pwd)
    assert rsp.status_code == 200
    #检查某个字段值是否存在
    #1.只检查关键文本信息的是否存在。
    assert 'id' in rsp.text

@allure.step
@pytest.mark.parametrize('usr,pwd',[('qwen','q1234567'),('qwen1','q123456')])
@pytest.mark.skipif(is_Not_Run,reason=Run_Reason)
def test_login_fail(usr,pwd):
    rsp = login_zhiguyichuan(usr, pwd)
    assert rsp.status_code == 200
    # 检查某个字段值是否存在
    assert 'id' not in rsp.text

def test_openId_index():
    """读取文件"""
    dict = readJson('../MidTokenVar.json')
    rsp = openId_index(dict.get('openId'),dict.get('token'))
    assert rsp.status_code == 200

def test_total():
    """读取文件"""
    dict = readJson('../MidTokenVar.json')
    rsp = totalHtml(dict.get('openId'),dict.get('token'))
    assert rsp.status_code == 200

#pytest 固件的概念。
#一个在整个工程，某个指定的变量名称，拥有一个值。
def test_openId_index_by_fixed(getOpenId,getToken):
    """使用固件"""
    rsp = openId_index(getOpenId,getToken)
    assert rsp.status_code == 200

def test_register_success():
    #需要确保注意的用户名，不在数据库中，所以需要调用数据层。
    username = DataUser.username_only()
    email = DataUser.email_only()
    rsp = register(username,'1',username,email,'1')
    assert 200 == rsp.status_code
    #2.接口大部分信息的检查，需要去数据库中进行检查。所以接口自动化测试的难度，在于对数据的管理与检查，与开发没有太大的区别
    assert DataUser.chk_email_exist(email) == True
