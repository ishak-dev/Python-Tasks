def rem(x, y):
    c=0
    x1=""
    for i in range(0, len(x)):
        if x[i]!=y:
            x1=x1+x[i]
        if x[i]==y:
            c+=1
            
    if c>0:
        return x1
    if c==0:
        return (x[:-1])
        
sen=(input("Please enter a sentence: "))
let=(input("Please enter a letter: "))
print(rem(sen, let))