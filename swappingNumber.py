a=float(input("Enter a Number:"))
b=float(input("Enter a Number:"))

#swapping must be happen with multiple ways so firstly by using temp varible.

print(f"A is {a} b is {b}  before swapping.")
temp=a
a=b
b=temp

print(f"A is {a} b is {b}  after swapping.")

#second way without using extra carible
print('\n\n SECOND METHOD\n\n')
print(f"A is {a} b is {b}  before swapping.")
a=a+b
b=a-b
a=a-b
print(f"A is {a} b is {b}  after swapping.")