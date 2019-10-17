from common.base import Base

class Reviews(Base):

    def review(self,text,num):
        '''评价+评星'''
        self.driver.find_element_by_xpath("//*[@text='待评价']").click()
        self.driver.find_element_by_id('com.tpshop.malls:id/order_show_btn').click()
        self.driver.find_element_by_xpath("//*[@text='请输入评价']").send_keys(text)
        stars = self.driver.find_elements_by_id(f'com.tpshop.malls:id/star{num}_btn')
        for i in stars:
            i.click()
        self.driver.find_element_by_xpath("//*[@text='提交']").click()


if __name__ == '__main__':
    from time import sleep
    review = Reviews()  # 实例化
    sleep(3)
    review.login(15360667898,123456)    # 输入用户名+密码
    sleep(2)
    review.review('欢乐时光就要开始了',5)    # 输入评价+评星
    sleep(2)
    review.quit()