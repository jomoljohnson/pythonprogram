word=input("Enter the string:")
list1=word[-3:]
if list1=="ing":
    x1=word.replace("ing","ly")
    print(x1)
else:
    x2=word.replace(list1,"ing")
    print(x2)
