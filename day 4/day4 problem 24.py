#leap year
'''
year=int(input())
if year%400==0:
    print("leap year")
else:
    print("not a leap year") '''

#find a leap year in a given range of year

a=int(input())
b=int(input())
for i in range(a,b):
    if i%400==0 or (i%4==0 and i%100!=0):
       print(i,end=" ")