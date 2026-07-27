while True:
    year = int(input("Enter year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

    choice = input("Do you want to check another year? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you!")
        break