import copy

class Bus:

    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = Bus(['alice','bill','clairs','david'])
# 浅复制
bus2 = copy.copy(bus1)
# 深复制
bus3 = copy.deepcopy(bus1)

bus1.drop('bill')
print(bus2.passengers)
print(bus3.passengers)
