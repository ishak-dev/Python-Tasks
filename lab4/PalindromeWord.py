def reverse(mystr):
    r = ""
    for char in mystr:
        r = char + r
    return r    

def check(mystr):
    if mystr == (reverse(mystr)):
        return True
    else:
        return False



print(check("budala"))    

