n=int(input("Enter the number:"))
x=0
i=2
while(i<n/2):
    if(n%i==0):
        x=1
        break
    i=i+1
if(x==0):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")