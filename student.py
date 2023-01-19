name=input("Enter the name:")
print("Enter the marks of 5 subjects")
total=0
for i in range(3):
    num=int(input("Enter the mark out of 200:"))
    total = total + num
print("total=",total)
print("percentage=",total/600*100)