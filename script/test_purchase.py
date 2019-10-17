from page.purchase_goods import PurchaseGoods
import pytest

@pytest.fixture()
class TestPurchaseGoods(PurchaseGoods):

    @pytest.mark.run(order=1)
    def test_purchase_goods(self):
        '''购买普通商品'''
        self.find_ele("//*[@text='航测试手机']")

    @pytest.mark.run(order=2)
    def test_purchase_goods2(self):
        '''购买活动商品'''
        self.find_ele("//*[@text='团购']")
        self.find_ele("//*[@text='凉鞋团购']")
        self.find_ele2("//*[@text='加入购物车']")
        self.find_ele2("//*[@text='确定']")
        self.find_ele2("//*[@text='购物车']")
        self.find_ele2("//*[@text='立即购买']")
        self.find_ele3([450,440])
        self.find_ele2("//*[@text='提交订单']")


if __name__ == '__main__':
    pytest.main('-s test_purchase.py')

