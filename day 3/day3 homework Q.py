#find even or odd
#find greatest of 3
#find sum of all the elements in an array

##find peak element in an array

#find maximum element in array
#find second maximum in an array
#find second largest element in an array
#reverse an array without using bulid in functions
#find the sum of squares of given number
#find sum of squares of even and odd digits
#check wheather given number is palindrom or not (using while loop)
#write a program to print first 10 fabinoci series

#1
n=int(input())
if(n%2==0):
    print('even')
else:
    print('odd')
#2
n1=int(input())
n2=int(input())
n3=int(input())
if (n1>=n2) and (n1>=n3):
    greatest=n1
elif (n2>=n3) and (n2>=n3):
    greatest=n2 
else:
    greatest=n3
print("the greatest number is",greatest)
#4
arr=[2,3,4,5,6]
max=arr[0]
for i in range(0,len(arr)):
    if(arr[i]>max):
        max=arr[i]
print(max)
#5
a=[]
n=int(input())
for i in range(1,n+1):
    b=int(input())
    a.append(b)
a.sort()
print("second largest element is:",a[n-2])
#7
arr=[1,2,3,4,5]            
rev_arr =[]
rev_arr=arr[::-1]
print(rev_arr)
#sum of all elements in array
n=10
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
#8
num=456
a=num%10
num=num//10
b=num%10
c=num//10
add=(a ** 2)+b(b ** 2)+(c ** 2)
print(add)
#10
n=int(input("enter a number"))
pal=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(pal==rev):
    print("palindrome number")
else :
    print("not a palinfrome number")
#9
n=int(input())
i=1
sum=0
while(i<=n):
    sum=sum+(i*i)
    i=i+1
print(sum)