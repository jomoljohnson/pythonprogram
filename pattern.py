i=1
n=int(input("Enter the limit:"))
while(i<=n):
    j=n
    while(j>=i):
        print("*",end="")
        j=j-1
    print("\n")
    i=i+1
