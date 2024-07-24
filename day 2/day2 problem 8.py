#given an space seperate integer list.find the aveage of elements present in the even index

my_list=list(map(int,input().split(" ")))
sum=0
count=0
n=len(my_list)
for i in range(len(my_list)):
    if(i%2==0):
       sum+=my_list[i]
       count+=1
print(sum/count) 

#write a program to find area of a circle
#write a program to find perimeter of a circle
#write a program to find area of a triangle
#write a program to find perimeter of a triangle