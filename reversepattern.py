n=int(input("Enter the limit:"))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print("*",end="")
        j=j+1
    print("\n")
    i=i+1
i=1
while(i<=n):
    j=n
    while(j>i):
        print("*",end="")
        j=j-1
    print("\n")
    i=i+1