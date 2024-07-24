#for loop syntax
my_list=list(map(int,input().split()))
for i in range(len(my_list)):
    print(my_list[i],end=" ")

print("\n-------------------")
for i in my_list:
 print(i,end=" ") 

s="hello world"
for i in range(len(s)):
    print(s[i],end="")
print()
for i in s:
    print(i,end="")

    '''
    # my_list=list(map(int,input().split()))
# for i in range(len(my_list)):
#     print(my_list[i],end="")
# print("\n")
# for i in my_list:
#     print(i,end="")

# s="hello world"
# for i in s:
#     print(i,end="")
# print('\n')
# for i in range(len(s)):
#     print(s[i],end="@")





list2=list(map(int,input().split()))
for i in range(len(list2)):
    print(list2[i],end=" ")
print("\n")
for i in list2:
    print(i,end=" ")
print("\n")
st="shivani singh"
for i in range(len(st)):
    print(st[i],end="")
print("\n")
for i in st:
    print(i,end="")
    '''
