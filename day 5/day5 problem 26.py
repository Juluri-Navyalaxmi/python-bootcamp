# input=hello123world , output=6
'''
a="0123456789"
inp=input()
c=0
for i in inp:
    if (i in a):
        c+=int(i)
print(c) '''

#reverse the number present in a given string
#input=hello1234 output=4321

a="0123456789"
n=input()
ans=""
rev=""
for i in n:
    if (i in a):
        ans+=i
print(ans)

 
