#problem 2
'''print the element in aparticular index 
input: k=8
       1 2 3 4 5
output:4 '''

'''
my_list=list(map(int,input().split(" ")))
k=int(input())
i=1
for i in range(i,len(my_list)):
    if(k>i):
        i=k%len(my_list)
        print(my_list[i+1])
        break
    else:
        print(my_list[i])
        break '''

'''
my_list=list(map(int,input().split(" ")))
k=int(input())
idx=k%len(my_list)
print(my_list[idx]) '''