def function(mystr):
    rever = ''
    for char in mystr:
        rever = char + rever
    return rever

def mirror(mystr):
    return mystr + function(mystr)


print(mirror("good"))        