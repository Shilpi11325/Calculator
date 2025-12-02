print ("======SIMPLE CALCULATOR======")
print ("1.ADD")
print ("2.SUBTRACT")
print ("3.MULTIPLY")
print ("4.DIVIDE")

choice = int (input("enter your choice (1-4):"))
a= float (input("enter first number:"))
b= float (input("enter second number:"))

if choice==1:
    print ("SUM=",a+b)
elif choice==2:
    print ("SUB=",a-b)
elif choice==3:
    print ("MUL=",a*b)
elif choice==4:
    if b==0:
        print ("ERROR!,cannot divide by 0.")
    else:
        print ("DIV=",a/b)
else:
    print ("INVALID CHOICE")