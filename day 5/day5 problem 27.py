#ASCII values
#to know the ascii value we use ord
'''
print(ord('A'))
print(chr(65))
print(ord('A')+3)
print(ord('<'))
print(chr(60)) '''

#special characters are 32 to 47(we are from 32 because we not need before ascii values)
'''
for i in range(32,128):
    print(chr(i),end=" ")  '''

#print sum of elements using ascii values
'''
inp=input()
c=0
for i in inp:
     if(ord(i)>=48 and ord(i)<=57):
        c+=int(i)
print(c) '''
        
#write a code to print all the capital letters in a given string
'''
inp=input()
for i in inp:
     if(ord(i)>=65 and ord(i)<=90):
        print(i)  '''

#remove all the brackets from the algebric expression
'''
inp=input()
for i in inp:
    if(ord(i)==41 or ord(i)==40 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="") '''
#or
'''
inp=input()
for i in inp:
    if(ord(i)!=41 and ord(i)!=40 and ord(i)!=91 and ord(i)!=93 and ord(i)!=123 and ord(i)!=125):
        print(i,end="") '''