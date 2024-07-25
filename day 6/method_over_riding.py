class Animal:
    def speak():
        return "speaking....."
class Dog(Animal):
    def speak():
       return "dog is speaking"
class Puppy(Dog):
    def speak():
        return "puppy is speaking....."
obj3=Puppy
print(obj3.speak())

'''
#her running is lost and hello is printed and last one will be printed
def run():
    return "running"
def run():
    return "hello"
print(run()) '''