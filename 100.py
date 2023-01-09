list=[]
n=int(input("Enter the limit:"))
for i in range(n):
    x=int(input("Enter the elements:"))
    if x>100:
        list.append("Over")
    else:
        list.append(x)
print(list)
