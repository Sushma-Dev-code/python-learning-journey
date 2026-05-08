def Menu():
    print("------Banking System------")
    print("1.Check balance\n2.Deposite\n3.Withdraw\n4.Exit")
balance=0
while True:
    Menu() 
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Balance : ",balance)
    elif choice==2:
        amount=int(input("Enter amount to deposit:"))
        balance +=amount
    elif  choice==3:
        amount=int(input("Enter amount to withdraw:"))
        balance -=amount
    elif choice==4:
        print("Thankyou for using banking System")
        break