def function(x):



     br = 1

     y = ""

     for i in range (0,len(x)):

          if (x[i] == x[i-1]):

              br = br +1 

              if (br>2 and br < 5):

                  y = y + x[i] + " " 

          else:
              br = 0   

                  

     return y



x = input("input string: ")

print(function(x))