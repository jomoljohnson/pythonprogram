n=int(input("Enter the limit:"))
i=1
for i in range(n):
    j=1
    for j in range(i):
        for j in range(i,-1):
            print("*",end=" ")
        print("\n")