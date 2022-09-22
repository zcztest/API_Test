

#简单复习一下，http协议->接口，95%都是以http协议为代表的
#有几个面试问题，容易被问题。

#1.http协议熟不熟悉？

#2.get和post的区别？

#3.响应的状态码有哪些?

#4.请求的常见包头有哪些？

#分为两部分。
#请求部分

#1. 请求的方法 请求的地址 请求的版本  ：必须要用的
#2. 请求的包头                      ：浏览器一般自带了一部分，当然也可以自己增加，增不增加是由服务端来决定的
#3. 请求的内容                      ：是非必填的

#响应部分

#1. 协议的版本  响应的状态码  reason
#2. 响应的包头
#3. 响应的内容                      :非必填的。

#做接口测试，常用的python包有哪些。
# httplib,httplib2,urllib,urllib2,urllib3[最新的],requests[最常用的90%],
# grequests[基于python协程的一个包],aiohttp[基于异步的],geventhttpclient

#pip install reqeusts

import requests

#如果我们想发送一个get请求
response = requests.get('https://www.qingshanzaixian.cn/hot',verify=False)
# #获取响应的状态码
print(response.status_code)#int
# print(response.headers)#dict
# print(response.text)#str
# print(response.content)#以二进制的形式获取响应的内容
# print(response.json())#只能在响应内容是json字符串的时候才可以使用。


#看一下源码，可以知道。get请求访问的是requests这个请求
#1. requests这个包的主要参加有哪些?
#method->get,post,put,delete,主要是根据我们的接口文档中的定义的方法来调用其相关的方法即可。
#url
#params->只能在get请求时使用。
#data，除get请求，其它请求都可以使用。
#json
#headers
#timeout
#file，上传文件的时候需要使用
#verify,如果是https，建议加上这个.verify=False的意思，就是在建立https连接的时候，不用进行ssl证书的信任过程

#2。什么时候用data,什么时候用json

#api文档里面，有一个content-type为application/x-www-form-urlencoded;charset=utf-8，时候才能使用。
#json，api文档里面有一个content-type为application/json，就要用json=

#3.他的响应属性和方法有哪些？
# print(response.status_code)#int
# print(response.headers)#dict
# print(response.text)#str
# print(response.content)#以二进制的形式获取响应的内容
# print(response.json())#只能在响应内容是json字符串的时候才可以使用。


# response5 = requests.post('http://amn.zhiguyichuan.com:9012/login',
#                           json={"userName":"qwen","passWord":"q123456"},
#                           headers={"X-Requested-With": "XMLHttpRequest"}
#                           )
# print(response5.text)

# response4 = requests.post('http://120.79.100.4:9013/user/login',data={"email": "gyppp@qq.com",
#                                                                       "password": 123456,
#                                                                       "code": 1111,'is_mt':0})
# print(response4.text)


# response2 = requests.get('http://amn.zhiguyichuan.com:9012/total/allUser/order?page=1&limit=1000')
# print(response2.text)
#
# response3 = requests.get('http://amn.zhiguyichuan.com:9012/total/allUser/order?',params={'page':1,'limit':1000})
# print(response3.url)
# print(response3.text)




