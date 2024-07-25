#multiple 
class Father:
    def Father_speak():
       return "father class"
class Mother:
    def mother_speak():
        return "mother class"
class kid(Father,Mother):
    def kid_speak():
       return "im kid.im having properties of mother class and father class"
obj1=kid
print(obj1.Father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())