def function(x):
    x = x.split(" ")
    br = 0
    for i in x:
        if i[-1] == "y":
            br +=1

    return br

x = "djey ba sery"
print(function(x))