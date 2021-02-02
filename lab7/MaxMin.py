file  = open("C:/Users/user/Desktop/Python/lab7/text1.txt","r")

for line in file:
    line =  line.split()
    min = 0
    i = 1
    max = int(line[i])
    while i<len(line):
        if (int(line[i])>max):
            max = int(line[i])
        
    print("Max is  " + max + " and Min is " + min)



