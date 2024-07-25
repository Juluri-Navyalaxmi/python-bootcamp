#create a class
'''
class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def mod(a,b):
        return a%b
    
    
#create a object
obj1=Myclass
obj2=Myclass
print(obj1.add(2,5))
print(obj2.sub(12,5)) '''



'''
class Myclass:
    def add(a,b):
        return a+b
    

obj1=Myclass
c=obj1.add(5,1) 
print(c) '''

#constructer
'''
class Myclass:
    def _init_(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b

obj1=Myclass
c=obj1.add(5,1) 
print(c) '''
#class variable and instance variable
class Myclass:
    cls_var="i am class variable"
    def add(a,b):
        ins_var="i am instance varaible"
        return a+b
        print(cls_var)
        print(ins_var_add)
    

obj1=Myclass
c=obj1.add(5,1) 
print(c)

      