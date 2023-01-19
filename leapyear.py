yr1=int(input("Enter the year:"))
yr2=int(input("Enter the end year:"))
print("Leap year between",yr1,"and",yr2,"is:")
for i in range(yr1,yr2+1):
   if i%4==0:
        print(i,"\n")
