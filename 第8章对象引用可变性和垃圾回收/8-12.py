class HauntedBus:

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)


if __name__=="__main__":
    # bus1 使用新建的 passengers
    bus1 = HauntedBus(['alice','bill'])
    print(bus1.passengers)
    bus1.pick('charlie')
    bus1.drop('alice')
    print(bus1.passengers)

    # bus2 使用默认的 passengers
    bus2=HauntedBus()
    bus2.pick('carrie')
    print(bus2.passengers)

    # bus3 使用默认的 passengers
    bus3=HauntedBus()
    print('bus3 ',bus3.passengers)
    bus3.pick('Dave')
    print('bus2 ',bus2.passengers)
    print(bus2.passengers is bus3.passengers)
    print(bus1.passengers)