n=input("enter the list of integers:")
list2=[]
mylist=x.split(" ")
print(mylist)
for i in mylist:
    if i<0:
        list2=list2.append(i)
print(list2)