def function():
    dictt = {"a":1,"b":2,"c":10}
    for akey in dictt.keys():
        if dictt[akey]<9:
            dictt[akey] = dictt[akey] * 2
    return dictt


print(function())