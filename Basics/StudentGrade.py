# check th egrade of students
while True:
    marks=int(input("Enter marks(0-100): "))

    if marks<0 or marks>100:
        print("please enter valid marks between 0 and 100.")
        continue
    
    if marks>=90:
        print("Grade A")
    elif marks>=75:
        print("Grade B")
    elif marks>=60:
        print("Grade c")
    elif marks>=35:
        print("Grade D")
    else:
        print("Fail")    
    choice=input("Do you want to check another student's grade? (yes/no):").lower()

    if choice != "yes":
        print("Thank You!")
        break    