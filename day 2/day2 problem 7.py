#you are given with a , seperated natural numbers 1 to 10 . print even numbers
'''
my_list=list(map(int,input().split(",")))
for i in range(1,len(my_list),2):
 print(my_list[i],end=" ") '''

#number of even number
'''
my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
 count+=1
 print(count) '''

 #your given with a space seperated integer list.find number of even and odd element in a given list
'''
my_list=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(my_list)):
    if my_list[i]%2==0:
        even+=1
    else:
        odd+=1
#print(odd)
#print(even)  
print(even,odd) '''

