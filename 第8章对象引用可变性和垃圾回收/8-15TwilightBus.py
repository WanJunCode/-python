class TwilightBus:
    def __init__(self, passengers):
        if passengers is None:
            self.passengers = []
        else:
            # 使用传入参数的引用
            # self.passengers=passengers

            # 使用构造函数 浅复制
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

if __name__=="__main__":
    basketball_team = ['sue', 'tina', 'maya', 'diana', 'pat']
    bus = TwilightBus(basketball_team)
    print(bus.passengers)
    bus.drop('sue')
    bus.drop('tina')
    print(bus.passengers)
    print(basketball_team)