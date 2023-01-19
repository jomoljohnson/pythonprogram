text=input("enter the text:")
list1=text.split(" ")
for i in list1:
    x=list1.count(i)
    x2=set(x)
    print("Occurnce of",i,"is:",x)
