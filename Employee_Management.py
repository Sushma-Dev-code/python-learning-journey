
import json
import os


class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary
        }


class EmployeeManagementSystem:

    FILE_NAME = "employees.json"

    def __init__(self):
        self.employees = self.load_employees()

    def load_employees(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                print("Error loading employee records.")
        return []

    def save_employees(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump(self.employees, file, indent=4)

    def add_employee(self):
        try:
            emp_id = input("Enter Employee ID: ").strip()

            if not emp_id:
                print("Employee ID cannot be empty.")
                return

            if any(emp["emp_id"] == emp_id for emp in self.employees):
                print("Employee ID already exists!")
                return

            name = input("Enter Employee Name: ").strip()
            department = input("Enter Department: ").strip()
            salary = float(input("Enter Salary: "))

            if not name or not department or salary < 0:
                print("Enter valid employee details.")
                return

            employee = Employee(emp_id, name, department, salary)

            self.employees.append(employee.to_dict())
            self.save_employees()

            print("Employee added successfully!")

        except ValueError:
            print("Invalid salary. Please enter a number.")

    def view_employees(self):
        if not self.employees:
            print("No employee records found.")
            return

        print("\n--- Employee Details ---")

        for emp in self.employees:
            print(
                f"ID: {emp['emp_id']} | "
                f"Name: {emp['name']} | "
                f"Department: {emp['department']} | "
                f"Salary: ₹{emp['salary']}"
            )

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ").strip()

        for emp in self.employees:
            if emp["emp_id"] == emp_id:
                print("\nEmployee Found!")
                print(emp)
                return

        print("Employee not found.")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ").strip()

        for emp in self.employees:
            if emp["emp_id"] == emp_id:
                try:
                    name = input("Enter new name: ").strip()
                    department = input("Enter new department: ").strip()
                    salary = float(input("Enter new salary: "))

                    if not name or not department or salary < 0:
                        print("Invalid employee details.")
                        return

                    emp["name"] = name
                    emp["department"] = department
                    emp["salary"] = salary

                    self.save_employees()
                    print("Employee updated successfully!")
                    return

                except ValueError:
                    print("Invalid salary.")

        print("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ").strip()

        for emp in self.employees:
            if emp["emp_id"] == emp_id:
                self.employees.remove(emp)
                self.save_employees()
                print("Employee deleted successfully!")
                return

        print("Employee not found.")

    def average_salary(self):
        if not self.employees:
            print("No employee records available.")
            return

        total = sum(emp["salary"] for emp in self.employees)
        average = total / len(self.employees)

        print(f"Average Employee Salary: ₹{average:.2f}")

    def run(self):
        while True:
            print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Average Salary")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                self.average_salary()
            elif choice == "7":
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.run()
