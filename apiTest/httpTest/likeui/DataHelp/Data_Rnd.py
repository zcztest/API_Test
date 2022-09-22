# coding:utf-8
import random
import allure


# 一些随机产生的数据
class DataRnd():

    @staticmethod
    def getRndEmail(kk=5, ext='@qq.com'):
        """随机产生邮箱"""
        rnd_int = random.randint(1000, 9000)
        rnd = random.choices('abcdefghijklmnopqrstuvwxyz', k=kk)
        return '%s_%d%s' % (''.join(rnd), rnd_int, ext)


    @staticmethod
    def getRndUser(kk=5):
        rnd_int = random.randint(1000, 9000)
        rnd = random.choices('abcdefghijklmnopqrstuvwxyz', k=kk)
        return '%s_%d' % (''.join(rnd), rnd_int)



if __name__ == "__main__":
    print(DataRnd.getRndEmail())
