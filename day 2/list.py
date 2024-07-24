#list
'''my_list=[1,2,3,4]
print(my_list)

my_list=[1,2,3,4]
print(*my_list)

my_list=[1,2,3,4]
print(*my_list,end="@") '''

#inserting
'''
my_list=[1,2,3,4]
my_list.append(9999)
print(*my_list) '''
'''
my_list=[1,2,3,4]
#my_list.insert(0,999)
#my_list.insert(8000,990)
#pop
#my_list.pop()
#my_list.pop(2)
#my_list.pop(77)
print(*my_list)
#length
#print(len(my_list)) '''
#appending
'''
my_list=[1,2,3,4]
my_list1=[5,6,7,8]
new_lst=my_list+my_list1
print(*new_lst) '''

#copying list
'''
my_list=[1,2,3,4]
new_lst=my_list.copy()
new_lst.pop()
print(*new_lst) '''

#no of times repeated
'''
my_list=[1,2,3,4,2,2]
cnt=my_list.count(2)
print(cnt) '''
#sorting
'''
my_list=[1,-2,3,4,-99]
my_list.sort()
print(*my_list) '''

#list as dynamic
'''
#my_list=list(map(int,input().split(" ")))
#my_list=list(map(int,input().split(",")))
#my_list=list(map(int,input().split("@")))
my_list=list(map(float,input().split(" ")))
print(*my_list) '''

#problem 1 
'''
if user enters 1 
                 then append
        enters 2
                 then pop 
        enters 3
                 then sort 
        enters 4
                 print good morning,enter the length of string '''

my_list=list(map(int,input().split(" ")))
choice=int(input())
if(choice==1):
    my_list.append(6)
    print(my_list)
elif(choice==2):
    my_list.pop(1)
    print(my_list)
elif(choice==3):
    my_list.sort()
    print(my_list)
else:
    print(f"good morning,{len(my_list)}")
