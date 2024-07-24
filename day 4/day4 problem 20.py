'''
for 
for
for can be used
for
   for
      for 
can't be used for complexcity case '''
'''
password verifier
mr x is trying to create a new password for his new instagram account
this are the required condition for creating a new password:
    1.minimum length is 8 and maximum length is 15
    2.only @,/ is allowed in a password(must include)
    3.no spaces are allowed 
    4.only alpha numerics are allowed
    5.you are suppose to print weak if length is exact 8 
                               medium_length is between 8 to 12 
                               strong if length is b/w 12 to 15
'''

password=input()
len=len(password)
'''
if len>8:
    
    if len<12:

        if len<15:
            print("strong")
        else:
            print(" ,")
    else:
        print("medium_length")
else:
    print("weak") '''
min_len=8
max_len=15
if min_len<=len<=max_len:
    print(password)
else:
    print("password should be between 8 to 15 ") 
str='@/'
count=0
for i in password:
    if i in str[0] or str[1]:
        count+=1
        break
    else:
        print(" only @ or / should be present")