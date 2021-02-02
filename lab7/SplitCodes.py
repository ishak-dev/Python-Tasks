file  = open("C:/Users/user/Desktop/Python/lab7/text.txt","r")
data  = file.readlines()

for line in data:
    word = line.split()

    print("Student "+ word[0] + word[1] + word[9] )
file.close()
        