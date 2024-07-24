#check how many ovels are in a given string

'''
check=['a','e','i','o','u']
count=0
inp=input()
for i in inp:
    if(i in check):
        count+=1
print(count) '''

#or
'''
check=['a','e','i','o','u']
count=0
i=input()
inp=i.lower()
for i in inp:
    if(i in check):
        count+=1
print(count)
'''
#write a program to print all the ovels and consonents
'''
check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i=input()
inp=i.lower()
for i in inp:
    if(i in check):
        count+=1
for i in inp:
    if(i in abc):
        c+=1
print(count)
print(c) '''

#OR
'''
check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i=input()
inp=i.lower()
for i in inp:
    if(i in check):
        count+=1
    elif(i in abc):
        c+=1
print(count)
print(c) '''

#print all ovels followed by consonents
'''
check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
i=input()
inp=i.lower()
for i in inp:
    if(i in check):
        print(i,end="")
for i in inp:
    if(i in abc):
        print(i,end="") '''

#or
'''
vowel=['a','e','i','o','u']
consonents="bcdfghjklmnpqrstvwxyz"
ans=""
i=input()
inp=i.lower()
for i in inp:
    if(i in vowel):
        ans+=i
for i in inp:
    if(i in consonents):
        ans+=i
print(ans) '''

#print the unique characters in a string
vowel=['a','e','i','o','u']
consonents="bcdfghjklmnpqrstvwxyz"
ans=""
i=input()
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
    
print(ans)