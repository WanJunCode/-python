def tag(name,*content,cls=None,**attrs):
    print(name)
    for c in content:
        print(c)
    if cls  is not None:
        print('cls = ',cls)
    for attr,value in attrs.items():
        print('attr = ',attr,' value= ',value)

tag('wanjun',12,25,'jun','wan',key1=12,key2=13)