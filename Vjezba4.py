list = ["1","2","3","4","-5"]

for i in range (0, len(list)):

    if int(list[i]) < 0:
        sum = 0
        sum = int(sum) + int(list[i])

print(sum) 