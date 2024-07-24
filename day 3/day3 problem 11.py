'''
find the max element in the given list
case 0:
       12 23 36 44 45 57
       57
case 1:
       56 78 -8 12 34 -99
       78 '''

my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(0,len(my_list)):
    if(max<my_list[i]):
        max=my_list[i]
        
print(max)
#assignment work from right to left 