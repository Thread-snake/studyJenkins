import unittest
import os
import time

from appium import webdriver
from com.wu.units.getElement import waitObject
from com.wu.units.readFileData import fileData

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class login(unittest.TestCase, fileData):

    def setUp(self):
        print("setUp...........")
        desired_caps = {
            # "app":PATH("../testAPK/com.douban.frodo_6.13.1_155.apk"),#设置了appPackage和appActivity就不需要用此项
            'appPackage': 'com.douban.frodo',
            'appActivity': 'com.douban.frodo.activity.SplashActivity',
            'platformName': 'Android',#设置平台
            'platformVersion': "5.0",#设置版本号
            'deviceName': 'emulator-5554'#设置手机ID
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        print("tearDown.......")
        

    def test_openLogin(self):

        print("startCase........")
        #读取测试数据
        xpath = self.getData("../resource/loginXpath.csv")
        userData = self.getData("../resource/loginData.csv")

        #设置显示等待时间
        getElement = waitObject(self.driver)

        left = getElement.getElement(xpath[0].localType, xpath[0].localXpath)
        mobile = getElement.getElement(xpath[1].localType, xpath[1].localXpath)
        password = getElement.getElement(xpath[2].localType, xpath[2].localXpath)
        login = getElement.getElement(xpath[3].localType, xpath[3].localXpath)

        #点击第三方登录
        left.click()

        mobile.send_keys(userData[0].userName)
        password.send_keys(userData[0].password)
        #点击登录
        login.click()



if __name__ == "__main__":
    unittest.main()
