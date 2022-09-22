# coding:utf-8
import pytest
import time
import os
if __name__ == "__main__":
    path = os.getcwd() + "/TestBussiness"

    #allure serve allurereport
    #allure serve -o ./
    choise = input('请选择模块：user--用户模块;all--所有模块:pay--支付模块')
    if choise == 'user':
        path = path+"/test_user.py"
    elif choise == 'all':
        pass
    pytest.main(['-s',path,'--alluredir','allurereport','--html=./reports/%sreport.html' % (str(int(time.time())))])
    # pytest.main(['-q', './Test_Bussiness/', '--html=./reports/%sreport.html' % (str(int(time.time())))])
    # os.system('allure serve allurereport')

    #1.A 接口返回的值，如何传递给 B接口  ****
    #2.数据库的检查，会根据业务的关系，而非常复杂。******
    #3.pytest当中的一些固件的操作。
