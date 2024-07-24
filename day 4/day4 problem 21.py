#peak element (important)
#slicing example: [1:2]
'''
example:(in notes)
        5 12 8 17 18
        peak is 12
'''
#for printing all the peak elements except first and last elements
'''
my_list=list(map(int,input().split(" ")))
n=len(my_list)
for i in range(1,n-1):
    if my_list[i-1]<my_list[i] and my_list[i]>my_list[i+1]:
       print(my_list[i],end=" ")
'''

#peak elements including first and last elements

my_list=list(map(int,input().split(" ")))
n=len(my_list)
count=0
for i in range(1,n-1):
    if my_list[i-1]<my_list[i] and my_list[i]>my_list[i+1]:
        count=i
if my_list[-1]>my_list[-2] and my_list[-1]>count:
        count=len(my_list)-1
print(my_list[count]) 