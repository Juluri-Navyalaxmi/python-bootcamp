'''
replace the elements in the array with a average of max and min elements
case 0:
       13 2 67 20 68
       68+2=70==35
       35 35 35 35 35 '''

my_list=list(map(int,input().split(" ")))
max=my_list[0]
min=my_list[0]
for i in range(0,len(my_list)):
    if(max<my_list[i]):
        max=my_list[i]
    else:
        min=my_list[i]
avg=(max+min)/2
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)