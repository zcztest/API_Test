# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as  EC
import time
# from SeleniumWebdriverPO.mylog import log
from mylog import log
# from SeleniumWebdriverPO.config import PAGE_TIMEOUT, ELEMENT_TIMEOUT
from config import PAGE_TIMEOUT,ELEMENT_TIMEOUT
from selenium.webdriver.common.action_chains import ActionChains


# 将一些查找、断言的方法进行了封装以及一些增强
class BaseDriver(object):
    def __init__(self, wd):
        self.webdriver = wd
        time.sleep(1)
        self.webdriver.maximize_window()
        self.webdriver.set_page_load_timeout(PAGE_TIMEOUT)

    def find(self, css_value, by=By.CSS_SELECTOR):
        log.info(css_value)
        try:
            return WebDriverWait(self.webdriver, ELEMENT_TIMEOUT).until(
                lambda x: x.find_element(by=by, value=css_value))
        except Exception as e:
            log.error(e)
            self.webdriver.get_screenshot_as_file('./result/error_%s.png' % int(time.time()))

    def finds(self, css_value, by=By.CSS_SELECTOR):
        log.info(css_value)
        try:
            return WebDriverWait(self.webdriver, ELEMENT_TIMEOUT).until(
                lambda x: x.find_elements(by=by, value=css_value))
        except Exception as e:
            log.error(e)
            self.webdriver.get_screenshot_as_file('./result/error_%s.png' % int(time.time()))

    def input(self, text, css_value, by=By.CSS_SELECTOR, isClear=True):
        element = self.find(css_value, by=by)
        if isClear: element.clear()
        element.send_keys(text)

    def click(self, css_value, by=By.CSS_SELECTOR):
        element = self.find(css_value, by=by)
        element.click()

    def house_click(self, house_css_value, click_css_value, by_house=By.CSS_SELECTOR, by_click=By.CSS_SELECTOR):
        """鼠标移动某个元素上面，并且点击某个元素"""
        ActionChains(self.webdriver).move_to_element(self.find(house_css_value, by=by_house)).perform()
        time.sleep(0.5)
        self.click(click_css_value, by=by_click)

    def is_element_exist(self, css_value, by=By.CSS_SELECTOR):
        try:
            self.find(css_value, by=by)
            log.info(css_value, "查找成功")
            return True
        except Exception as e:
            log.info(e)
            self.webdriver.get_screenshot_as_file('./result/error_%s.png' % int(time.time()))
            return False

    def is_element_not_exist(self, css_value, by=By.CSS_SELECTOR):
        try:
            self.find(css_value, by=by)
            log.info("%s该元素本不该存在，但这个元素存在了" % (str(css_value)))
            self.webdriver.get_screenshot_as_file('./result/error_%s.png' % int(time.time()))
            return False
        except Exception as e:
            return True

    def is_text_in_pagesource(self, text):
        for x in range(10):
            result = text in self.webdriver.page_source
            if not result:
                log.info('没有找到' + text)
                time.sleep(1)
            return result

    def is_text_in_element(self, css_value, text, by=By.CSS_SELECTOR):
        if text in self.find(css_value, by=by).text:
            return True
        self.webdriver.get_screenshot_as_file('./result/error_%s.png' % int(time.time()))
        return False

    def get(self, url):
        for x in range(10):
            try:
                log.info(url)
                self.webdriver.get(url)
                self.webdriver.implicitly_wait(5)
                return self.webdriver
            except Exception as e:
                log.info(e)
        return self.webdriver
