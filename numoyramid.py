n=int(input("Enter the limit:"))
i=1
for i in range(n):
    j=1
    for j in range(i):
        print("*",end="")
        j=n
        for j in range(n):
            i=n
            for j in range(i):
                print("*",end="")
