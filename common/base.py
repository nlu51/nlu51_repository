# 导包
from appium import webdriver

class Base:
    # 配置启动参数
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "127.0.0.1:5555",   # U8ENW17C14007440
        "appPackage": "com.tpshop.malls",
        "appActivity": ".SPMainActivity", #.activity.person.user.SPLoginActivity
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "noReset": True
    }
    def __init__(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desired_caps)    # 打开App


    def find_ele3(self,element,duration=5000):
        '''查找元素'''
        self.size = self.driver.get_window_size()  # 获取手机屏幕大小
        self.width = self.size["width"]  # 获取手机宽
        self.height = self.size["height"]  # 获取手机屏幕高
        start_x = self.width * 0.5
        start_y = self.height * 0.5
        end_y = self.height * 0.9
        while True:
            try:
                self.driver.find_element_by_xpath(element).click()  # 点击找到的元素
                break
            except:
                self.driver.swipe(start_x, end_y, start_x, start_y, duration)  # 向下滑动

    def wait(self, act=desired_caps['appActivity']):
        '''等待页面加载完毕'''
        self.driver.wait_activity(activity=act, timeout=5, interval=5)

    def find_ele_by_id(self,element):
        '''通过id定位元素'''
        self.wait()
        return self.driver.find_element_by_id(element)
    def find_eles_by_id(self,elements):
        '''通过id定位一组元素'''
        self.wait()
        return self.driver.find_elements_by_id(elements)

    def find_ele_by_xpath(self,element):
        '''通过xpath定位单个元素'''
        self.wait()
        return self.driver.find_element_by_xpath(element)

    def tap(self,element):
        '''通过坐标定位元素'''
        self.driver.tap(element)

    def quit(self):
        '''退出App'''
        self.driver.quit()

if __name__ == '__main__':
    from time import sleep
    b = Base()
    b.find_ele_by_xpath('//*[@text="航测试手机"]')
    b.quit()
