class Human:
    def __init__(self,name, age):
        print("Constructor is called", name)
        self.name=name
        self.age=age

    def walk(self):
        print(f"{self.name} is walking")

c=Human("Sushma",22)
d=Human("sun", 20) 
c.walk() 
d.walk()
Human.walk(c)

class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f" My name is {self.name} i am {self.age} years old.")
#creating an object 
person1= Person("Arjun", 22) 
person1.introduce()

class movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    def display(self):
        print(f"movie Title is {self.title} and its Rating is {self.rating}")
m1=movie("Rajahuli",4)
m2=movie("KJF", 5)
print(m1.rating)
m1.display()
m2.display()

