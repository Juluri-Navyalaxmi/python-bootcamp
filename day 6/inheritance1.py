class Animal:
    def Speak():
        return "animal is speaking"
#single inh
class Dog(Animal):
    def Bark():
       return "Bow..."
class Puppy(Dog):
    def Puppy_speak():
        return "im puppy"

obj1=Animal
obj2=Dog
obj3=Puppy
#print(obj1.Speak())
#print(obj2.Bark())
'''
print(obj3.Bark())
print(obj3.Puppy_speak()) '''
