file  = open("C:/Users/user/Desktop/Python/lab7/text1.txt","r")
for line in file:
    line =  line.split()
    min = 20
    max = 0
    i = 1
    while i<len(line):
        if(int(line[i]) > max):
            max = int(line[i])
        elif (int(line[i]) < min):
            min = int(line[i])
        i += 1
    print("Max is " + str(max) + " Min is " + str(min))    
file.close()