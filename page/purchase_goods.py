from common.base import Base
from time import sleep

class PurchaseGoods(Base):

    def purchase_goods(self,goods_name):
        '''定位商品'''
        self.driver.find_element_by_id('com.tpshop.malls:id/category_tv')   # 进入分类
        self.find_ele(element=goods_name)
        sleep(2)
        self.find_ele2("//*[@text='立即购买']")
        sleep(1)
        self.find_ele2("//*[@text='确定']")
        sleep(1)
        self.find_ele2("//*[@text='提交订单']")
        sleep(3)
        self.find_ele2("//*[@text='货到付款']")
        sleep(1)
        self.find_ele2("//*[@text='完成']")
        self.quit()

if __name__ == '__main__':
    purchase = PurchaseGoods()
    purchase.login(15360667898,123456)
    purchase.purchase_goods("//*[@text='航测试手机']")
    purchase.quit()
