#problem
''' x goes to market 
10 apples         2 dozen bananas         8 oranges
cost   :  1 apple=15    1 orange=5           1 banana=4
x mother gave him 700
 left amount ?? 

amt=int(input())
app=int(input())
org=int(input())
ban=int(input())
tc=0
tc=app*15+org*8+ban*4
if(tc>amt):
  print("cheated")
else:
  print("not cheated") '''
#(or)

amt=int(input())
app=int(input())
org=int(input())
ban=int(input())
ct_app=15
ct_org=5
ct_ban=4
sum=(app*ct_app)+(org*ct_org)+(ban*ct_ban)
print(sum)
if(sum>amt):
  print("cheated")
else:
  print(" not cheated") 