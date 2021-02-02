def remove(x):
    r = x[0]
    for char in x[1:]:
        if char != r[-1]:
            r += char
    print(r)        
           






remove("sssyyynnnooopppsssiiisss")    