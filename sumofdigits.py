n=int(input("Enter the number:"))
sum=0
for i in range(n):
    x=n%10
    sum=sum+x
    n=n//10
print("Sum of digits  is:",sum)