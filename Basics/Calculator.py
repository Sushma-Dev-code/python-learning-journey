def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def displaymenu():
  print("### Simple Calculator ###")
  print("1.Add\n2. Subtract\n3. Multiply\n4.Quite")
    
while(True):
 displaymenu()
 choice =int(input("Enter your choice:"))

 if choice in {1,2,3,4,}:
    
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

 if choice==1:
    print("Result: ",add(a,b))
 elif choice==2:
    print("Result: ",sub(a,b))
 elif choice==3:
    print("Result: ",mul(a,b))
 elif choice==4:
    print("Quitting")
    break
 else:
    print("invalid choice.Try again")


    