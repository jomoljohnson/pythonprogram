n=int(input("Enter the limit:"))
sum1=0
sum2=0
for i in range(n+1):
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
print("Sum of even number:",sum1)
print("Sum of odd number:",sum2)