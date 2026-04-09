n=input("Enter any word :")
s=n[::-1]
if(n==s):
    print("string is palindrome ")
else:
    print(" String is not a palindrome")

#Second method..
rev=""
for char in n:
    rev=char+rev

if(rev==char):
    print("palindrome")

else:
    print("Not palindrome")
    
