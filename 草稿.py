# 1.导入appium
from appium import webdriver
from time import sleep

# 2.配置启动参数
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1：21503",
    "appPackage": "com.microvirt.launcher",
    "appActivity": ".Launcher",
    "noReset":True
}
# 3.打开APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
sleep(3)

# 4.使用swipe滑动
size = driver.get_window_size()  # 获取手机屏幕大小
width = size["width"]  # 获取手机宽
height = size["height"]  # 获取手机屏幕高
start_x = width * 0.5
start_y = height * 0.5
end_y = height * 0.9
# while True:
#     try:
#         driver.find_element_by_xpath("//*[@text='航测试手机']").click()  # 点击找到的元素
#         break
#     except:
#         driver.swipe(start_x, end_y, start_x, start_y, duration=2000)  # 向下滑动
#         print(1)

# driver.swipe(250,800,250,300,1000)
driver.swipe(start_x, end_y, start_x, start_y, duration=2000)  # 向下滑动
print(1)
sleep(5)
# 5.关闭APP
driver.quit()

#[30,328][510,403]  输入支付密码
#[450,436][540,484] 使用余额
#[450,367][540,415] 输入积分
# 酒
