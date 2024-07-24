# find prime or not using square
'''
for loop
          r=root of 7=2.64              r=root of 21=4.5
          2.64+1=3.64=3                 4.5+1=5.5=5
if condition 
                                        2,3,4
                                        21%2==0 not satisfes
                                        21%3==0 satisfies
                                        count+=1
'''
'''
n=int(input())
r=n**0.5
count=0
if n==1:
    print("not a prime number")
elif n==2:
     print("prime number")
for i in range(2,int(r+1)):
    if n%i==0:
        count=1
        break
if count==0:
        print("prime")
else:
     print("not prime")
'''
#write a program to print all the prime number in a given range
a=int(input())
b=int(input())
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
         print(i,end=" ")
          