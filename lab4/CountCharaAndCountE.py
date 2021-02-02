def function(string):
    lows = "abcdefghijkljmnjoprstuvzwxy"
    ups = "ABCDEFGHIKLJMNOPRSTUVZWXY"
    n = 0
    b = 0
    for x in string:
        if x in lows or x in ups:
            n+=1
            if x == "e" or x == "E":
                b+=1
    percent = ((b/n)*100)
    print ("text containts: ",n,"of which ", b ,"(",percent," )", "is ", "E")        





function("Keeeako je lijep dan Bozee")    