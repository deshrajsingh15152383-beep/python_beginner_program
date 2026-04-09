n=int(input("Enter a number:"))
original=n
temp=n
count=0

while(n!=0):
    n=n//10
    count+=1


for i in range(0,10):
    digit=0
    temp=original
    for j in range(count):
        if(temp%10==i):
            digit+=1
        temp=temp//10
    if(digit>0):
        print(f"number of {i} in {original} is {digit}")
    
