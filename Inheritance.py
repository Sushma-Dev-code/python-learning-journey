class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    pass
d=Dog()
d.speak() 

class User:
    def __init__(self,username):
        self.username=username
    def login(self):
        print(f"{self.username} logged in")

class Admin(User):
    def delete_User(self):
        print("Admin deleted the user")
a=Admin("Sushh")
print(a.username)  
a.login()
a.delete_User()    
