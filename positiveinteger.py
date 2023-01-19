#///////////////////////////////even numbers1//////////////////////////
#n=int(input("Enter the limit:"))
#list=[]
#list=[i for i in range(n) if i>0]
#print(list)
#////////////////square of n numbres2/////////////////////////////
#n1=int(input("Enter the limit:"))
#list1=[]
#list1=[i*i for i in range(n1+1)]
#print(list)
#/////////////////////vowels in a given word3////////////////////////////
#text=input("Enter the text:")
#word=["a","e","i","o","u"]
#for i in text:
#    j=i.split(",")
#    for x in word:
#        s=x.split(",")
#        if j==s:
#            print(s)
#//////////count of words4////////////////////////////////////
#///////////////////////leap year5/////////////////////////////////
#yr1=int(input("Enter the year:"))
#yr2=int(input("Enter the end year:"))
#print("Leap year between",yr1,"and",yr2,"is:")
#for i in range(yr1,yr2+1):
 #   if i%4==0:
  #      print(i,"\n")
#//////////////integer over 100-6//////////////////////////////////
#list=[]
#n=int(input("Enter the limit:"))
#for i in range(n):
#    x=int(input("Enter the elements:"))
#    if x>100:
#        list.append("Over")
#    else:
#        list.append(x)
#print(list)
#/////////////////////occurence of a-7///////////////////
#list=input("Enter the names:")
#x=list.split(" ")
#print(x)
#count=0
#for i in x:
#    j=i.split(",")
#    print(j)
#    for j in i:
#        if j=="a":
#            count=count+1
#print("Number of 'a' in each name is:",count)
#//////////////////string-8//////////////////////////
word=input("Enter the word:")
a = word[0]
for i in word:
        if i==a:
                word=word.replace(i,"$")
                word=a+word[1:]
print(word)
#////////////////////////evennumber-9/////////////////
#n=input("Enter the limit:")
#list1=[]
#for i in range(n):
#    list =int(input("Enter th elememnts:"))
#    if i%2==0:
        #list1.append(i)
#print(list1)
#/////////////////////////sumof all item in list-10////////////////////////
#x=int(input("Enter the limit:"))
#list1=[]
#for i in range(x):
#    x=int(input("Enter the elements:"))
#    list1.append(x)
#print("Sum:",sum(list1))
#///////////////////////////////numberpyramid-11////////////////
#n=int(input("Enter the limit:"))
#i=1
#for i in range(n):
#   j=1
#    for j in range(i):
#        print("*",end="")
#        j=n
#        for j in range(n,-1):
#            i=n
#            for j in range(i):
#                print("*",end="")
#///////////////////////////////////////////number of characters////////////////
#n=input("Enter the string:")
#list2=[]
#list=n.split(" ")
#for i in list:
#    i=i.split(",")


