list1=input("Enter the 1 list items:")
list2=input("Enter the 2 list items:")
if len(list1)==len(list2):
    print("2 List have  same lenght")
else:
    print("lists have not same lenght")
x1=list1.split(",")
sum1=0
for i in x1:
    sum1=sum1+i
x2=list2.split(",")
for i in x2:
    sum2=sum2+i
if sum1==sum2:
    print("Lists are same sum",sum1)
else:
    print("List are different sum",sum1,sum2)
sum2=0
set1=set(list1)
set2=set(list2)
set3=set1-set2
set4=set2-set1
set4=set3+set4
list3=list(set4)
print("Same elements in 2 list is:",list3)