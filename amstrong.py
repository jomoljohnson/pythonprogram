x1=int(input("Enter the low range:"))
x2=int(input("Enter the end range:"))
for n in range(x1,x2+1):
    sum=0
    temp=n
    while(temp>0):
        x=temp%10
        sum=sum+x**3
        temp=temp//10
    if n==sum:
        print(n)