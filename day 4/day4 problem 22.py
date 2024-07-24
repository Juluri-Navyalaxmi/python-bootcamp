#GCD of 2 numbers
#Euclidean Algorithm:
'''
step1      step2          step3
a=5        a'=15          a''=5
b=15       b'=5%15=5      b''=5%5=0
'''
'''
a=int(input())
b=int(input())
while b!=0:
    a,b=b,a%b
print("gcd is ",a)
'''
#LCM of 2 numbers
a=int(input())
b=int (input())
gcd=0
lcm=0
c=a*b
while b!=0:
    a,b=b,a%b
gcd=a
lcm=(c)/gcd

print(lcm)