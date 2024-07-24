# while -> it is used to reduce the size

'''sum of digits:
   123 1+2+3=6
   123%10=3
   3
   123/10=12
-------------------------------
   n=12
   12%10=2
   3+2=5
   12/10=1
--------------------------------
   n=1
   1%10=1
   5+1=6
   1/10=0   
---------------------------------
n=0 goes on working  
so we use // to over come it '''

'''
n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r #important
    n=n//10
print(sum) '''

# find the sum of squares of digit in a number 

'''
n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum) '''

#sum of elements of even values
'''
n=int(input())
sum=0
while n>0:
    r=n%10
    if r%2==0:
      sum=sum+r
    n=n//10
print(sum) '''


'''
how to reverse a number 
123
321   '''

n=int(input())

while n>0:
    r=n%10
    print(r,end="")
    n=n//10 

'''
n=int(input())
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(rev))
#print(int(rev)) '''