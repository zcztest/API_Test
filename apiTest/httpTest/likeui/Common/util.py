#常用的一些底层公共函数
import hashlib
from httpTest.likeui.mylog import log
import json


def md5( str):
    m = hashlib.md5(str.encode(encoding='utf-8'))
    return m.hexdigest()

def logHttpRst(fun):
    """记录http请求中的请求和返回信息"""
    def wapper(*args,**kwargs):
        result = fun(*args,**kwargs)
        log.info(result.url)
        log.info(result.headers)
        log.info(result.request.body)
        log.info(result.status_code)
        log.info(result.text)
        log.info('-----------------------------')
        return result
    return wapper

def readJson(filepath):
    with open(filepath) as f:
        return json.loads(f.read())

def writeJson(filepath,dict):
    with open(filepath,'w') as f:
        f.write(json.dumps(dict))