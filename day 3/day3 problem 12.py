#find the minimum element in a given list
my_list=list(map(int,input().split(" ")))
min=my_list[0]
for i in range(0,len(my_list)):
    if(min>my_list[i]):
        min=my_list[i]
        
print(min)