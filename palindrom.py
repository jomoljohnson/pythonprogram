num=int(input("Enter the number:"))
rev=0
str=num
while(num>0):
    x=num%10
    rev=rev*10+x
    num=num//10
if str==rev:
    print("Number is palindrom")
else:
    print("Number is not Palindrom")