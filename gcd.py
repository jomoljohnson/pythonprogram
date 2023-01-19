num1=int(input("Enter 1 number:"))
num2=int(input("enter 2 number:"))
i=1
while(i<=num1 and i<=num2):
    while(num1%i==0 and num2%i==0):
        gcd = i
        print("GCD of 2 number are",gcd)
    i=i+1