

for i in range(1,5):
  for j in range(1,5):
    if (i == 2 and (j==2 or j==3)):
      print(" ", end=" ")
    elif (i == 3 and (j==2 or j==3)):
      print(" ", end=" ")
    else:
       print("#", end=" ")
  print()  
