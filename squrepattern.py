n=int(input("Enter the limit:"))
i=1
for i in range(n):
    j=i
    for j in range(i):
        print(j*i,end="")
    print(" ")