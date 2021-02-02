def function():
    for i in range(0,4):
        for j in range(0,4):
            if ((i==1 or i==2) and (j==1 or j==2)):
                print(end=" ")
            else:
                print("*", end="") 
        print(" ")           

function()
