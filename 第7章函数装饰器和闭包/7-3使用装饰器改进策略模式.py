promos=[]

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

@promotion
def BulkItem_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def LargeOrder_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    discount_items = {item.product for item in order.cart}
    if len(discount_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    return max(promo(order) for promo in promos)