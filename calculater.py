num1=int(input("Enter the 1 number:"))
num2=int(input("Enter the 2 number:"))
i=int(input("Enter the options 1.Add\n2.Sub\n3.Mul\n4.Div\n"))
if(i==1):
    print("Add= ",num1+num2)
elif(i==2):
    print("Sub= ",num1-num2)
elif(i==3):
    print("Mul= ",num1*num2)
elif (i==4):
    print("Div= ",num1/num2)
if(i>5):
        print("Error")