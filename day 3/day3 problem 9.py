#problem1
'''find the elements that is present in k+n index
input: k=3 and n=2
       3 6 8 61 2 
output: 2
          ---------------
input: k=2 and n=4
       80 70 54 36 72
output:ERROR '''

'''
my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
len=len(my_list)
if len < k+n:
   print("ERROR")
else:
   for i in range(len):
      if(i==k+n):
        print(my_list[i])
        break
     #my_list(k+n) '''   

