from common.base import Base

class Login(Base):

    def login(self, username, password):
        self.driver.find_element_by_xpath("//*[@text='我的']").click()    # 点击个人中心
        self.driver.find_element_by_id('com.tpshop.malls:id/head_img').click()    # 点击登录/注册
        self.driver.find_element_by_xpath("//*[@text='请输入账号']").send_keys(username)   # 输入账号
        self.driver.find_element_by_id('com.tpshop.malls:id/pwd_et').send_keys(password)    # 输入密码
        self.driver.find_element_by_id('com.tpshop.malls:id/login_tv').click()   # 点击登录

    def logout(self):
        self.driver.find_element_by_id('com.tpshop.malls:id/title_back_img').click()    # 返回上一层
        self.driver.find_element_by_id('com.tpshop.malls:id/setting_btn').click()    # 点击设置
        self.driver.find_element_by_id('com.tpshop.malls:id/exit_tv').click()    # 点击退出账户
        self.driver.quit()  # 退出app

if __name__ == '__main__':
    login = Login()
    login.login(15360667898,123456)
    login.logout()