file  = open("C:/Users/user/Desktop/Python/lab7/text1.txt","r")

for line in file:
    line =  line.split()
    average = 0
    z = 0
    i = 1
    while i<len(line):
        average += int(line[i])
        i += 1
    z = average/i
    print("average exam score for student " + line[0] + " is " + str(round(z, 2)))



