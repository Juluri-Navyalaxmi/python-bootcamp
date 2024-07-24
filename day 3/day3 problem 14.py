'''
   find the missing number in an array
   like given sequence of number (1 to 10)
   1 2 3 4 6 7 8 9 10
   '''

my_list=list(map(int,input().split()))
n=int(input())
t=n*((n+1)/2)
sum=0
mis=0
for i in range(len(my_list)):
    sum+=my_list[i]
mis=t-sum
print(mis)

