class Parent:
    def show(self):
        print("parent method")
class child(Parent):
    def show(self): 
        print("Child method")
c=child()  
c.show()
p=Parent()
p.show()     