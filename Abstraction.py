from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(Vehicle):
        def start(self):
            print("Car is started")
class Bike(Vehicle):
        def start(self):
            print("Bike is started")
c=car()
c.start()

b=Bike()
b.start()
#Payment System Example
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")

p1 = UPI()
p1.pay(500)

p2 = Card()
p2.pay(1000)

 #Shape Area Example
from abc import ABC,abstractmethod
 
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
         print("Area of circle")
class Rectangle(Shape):
     def area(self):
          print("Area of rectangle")
c=Circle()
c.area()

r=Rectangle()
r.area()

#Login System Example
from abc import ABC, abstractmethod

class Login(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class GoogleLogin(Login):
    def authenticate(self):
        print("Login using Google")

class FacebookLogin(Login):
    def authenticate(self):
        print("Login using Facebook")

GoogleLogin().authenticate()
FacebookLogin().authenticate()

#Employee Salary Example
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class Developer(Employee):
    def salary(self):
        print("developer Salary is:50k")
class Manager(Employee):
    def salary(self):
        print("Manager Salary is:50k")
Developer().salary()
Manager().salary()     