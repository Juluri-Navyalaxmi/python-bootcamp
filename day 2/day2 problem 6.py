#take a space seperate input from user and print alternate elements

my_list=list(map(int,input().split()))
for i in range(0,len(my_list),2):
   print(my_list[i],end=" ") 

#problems 0n list
#my_list1=list(map(str,input().split(",")))
#print(*my_list)
#print(my_list.count())

#print 1 to 100 numbers using for loop
#num=int(input())
#for i in range(1,num+1):
    #print(i)
#using for loop append 1 to 100 number
#n=int(input())
#list=[]
#for i in range(1,num+1):
    #list.append()
   # print(list,end="")
# find sum of all numbers in list
#list1=list(int(input().split("")))
#sum=0
#for i in range(len(list1)):
    #sum+=list1[i]
    #print(sum)
#take a space seperated input from user and print alternate elements
'''my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
 print(my_list[i],end="")
 count+=1
 print(count)'''
 
#given an space seperate integer list find the avg of elements in the present in the even index
'''my_list=list(map(int,input().split()))
sum=0
count=0
n=len(my_list)
avg=0
for i in range(len(my_list)):
    if(i%2==0):
        sum+=my_list[i]
        count+=1
        avg=sum/len(my_list)
print(sum/count)''''''


