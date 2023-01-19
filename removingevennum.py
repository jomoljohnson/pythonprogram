n=int(input("Enter the size of array:"))
print("Entere the elemts:")
list=[]
for i in range(0,n):
    x=int(input())
    if(x%2==0):
        list.append(x)
print("Removed even numbers are:",list)