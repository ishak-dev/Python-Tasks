def  function(n):
    if n<= 1:
        return n
    else:
        return n + function(n-1)


n = 16


if n < 0:
    print("Entere a positive number")
else:
    print("The sum is ",function(n))    