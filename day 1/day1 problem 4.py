#problem 2
'''take input from the user 
if it is +ve and even
        print +ve but even
if it is +ve and odd
        print  +ve but odd
if it is negative and even
        print even but negative
if it is negative and odd
        print negative but odd '''


n=int(input())
if (n>0 and n%2==0):
    print("+ve even number")
elif (n>0 and n%2!=0):
     print("+ve odd number") 
elif (n<0 and n%2==0):
     print("-ve even number")
else:
    print("-ve odd number")  
      