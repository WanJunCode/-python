from abc import ABC,abstractmethod
from collections import namedtuple
import inspect

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    """单个的商品"""
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:
    """订单"""
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
        self.total_money=None

    def total(self):
        if self.total_money is None:
            self.total_money = sum(item.total() for item in self.cart)
        return self.total_money

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            # self.promotion is an instance of Promotion
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

def Fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def BulkItem_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def LargeOrder_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    discount_items = {item.product for item in order.cart}
    if len(discount_items) >= 10:
        return order.total() * .07
    return 0

promos=[globals()[name] for name in globals()
        if name.endswith('_promo')
        and name !='best_promo']

def best_promo(order):
    return max(promo(order) for promo in promos)

joe=Customer('John Doe',0)
ann=Customer('Ann',1050)
cart=[LineItem('banana',4,.5),
     LineItem('apple',10,1.5),
     LineItem('watermellon',5,5.0)]
print(Order(joe,cart,best_promo))
print(Order(ann,cart,best_promo))
