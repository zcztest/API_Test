import time
import pytest,os
from httpTest.likeui.mylog import log
from httpTest.likeui.Common.util import writeJson,readJson

ENV = "测试环境"
VERSION = "1.0"
TEST_HOST = 'http://120.79.100.4:9013'
TEST_HOST_2 = 'http://amn.zhiguyichuan.com:9012'
# 打开新项目，新的接口测试项目
TEST_HOST_3 = "http://127.0.0.1:8888/api/private/v1/"

MYSQL_User = 'new_shop'
MYSQL_PWD = 'KEXcas2bWpsNe4T3'
MYSQL_HOST = '120.79.100.4'
MYSQL_DB = 'new_shop'

is_Not_Run = False
Run_Reason = "调试时不执行"

@pytest.fixture(autouse=True)
def record_run_time():
    """该模块下所有的测试案例自动加载此函数，并获取运行时间"""
    t1 = time.time()
    yield
    log.info('该案例运行环境={0},版本={1},时间为＝{2}'.format(ENV, VERSION, time.time() - t1))

@pytest.fixture()
def getOpenId():
    result = readJson('../MidTokenVar.json')
    return result.get('openId')

@pytest.fixture()
def getToken():
    result = readJson('../MidTokenVar.json')
    return result.get('token')
