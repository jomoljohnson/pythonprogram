n1=0
n2=1
n3=n1+n2
i=3
num=int(input("Enter the limit:"))
print(n1,"\n",n2)
while(i<num):
    print(n3)
    n1=n2
    n2=n3
    n3=n1+n2
    i+=1
