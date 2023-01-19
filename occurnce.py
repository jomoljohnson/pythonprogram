list=input("Enter the names:")
x=list.split(" ")
print(x)
count=0
for i in x:
    j=i.split(",")
    for j in i:
        if j=="a":
            count=count+1
print(count)
