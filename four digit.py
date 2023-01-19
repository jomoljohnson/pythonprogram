n1=int(input("Enter the 4 digit starting range:"))
n2=int(input("Enter the 4 digit ending range:"))
list1=[]
for i in range(n1,n2):
    if i%2==0:
        for j in range(1,i):
            if j*j==i:
                list1.append(i)
print(list1)
if len(list1)==0:
    print("")