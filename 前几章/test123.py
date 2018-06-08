class newclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def fangfa(self):
        if not hasattr(self,'age2'):
            print('设置...')
            self.age2=self.age+1
        else:
            print('already have')
        print(id(self.age2))
        return self.age2

wanjun=newclass('wan',12)
wanjun.fangfa()
print(wanjun.fangfa())