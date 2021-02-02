file  = open("C:/Users/user/Desktop/Python/lab7/text1.txt","r")
for line in file:
    line =  line.split()
    if(len(line)-1 >6):
        print(line[0] + "had" + str(len(line)-1) + "exam values")