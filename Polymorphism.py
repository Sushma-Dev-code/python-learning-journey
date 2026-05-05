class Cat:
    def sound(self):
        print("meow")
class Dog:
    def sound(self):        
        print("bark")
for animal  in(Cat(), Dog()):
    animal.sound()
