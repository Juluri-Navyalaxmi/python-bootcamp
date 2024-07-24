#input=ABC and 4   output=EFG
'''
inp=input()
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
       print(chr(ord(i)+4),end="") '''   

#print hifen for number of times
#print("-"*30)

#input=hello-----wor----ld , output=---------helloworld
'''
inp=input()
r="-"
for i in inp:
    if(i==r):
       print(i,end="")
for i in inp:
    if(i!=r):
       print(i,end="") '''
#or
'''
inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans) '''