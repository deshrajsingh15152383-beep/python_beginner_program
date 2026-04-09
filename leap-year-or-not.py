n=int(input("Enter a number:"))

if((n%4==0)and (n%100!=0) or (n%400==0)):
    print(f" Entered year is Leap Year")
else:
    print(f" Entered year is  NOT Leap Year")