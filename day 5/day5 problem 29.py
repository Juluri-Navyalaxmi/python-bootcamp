# i=number of rows and j=number of columns
'''
*****
*****
*****
*****
***** '''
'''
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ") 
    print()  '''

'''
*****
****
***
**
*    '''
'''
for i in range(n):
    for j in range(n-i):
        print("*",end=" ") 
    print() '''

'''
*
**
***
****
*****  
 '''
'''
for i in range(n):
    for j in range(i+1):
        print("*",end=" ") 
    print() '''

'''
  * * * *
*   * * *
* *   * *
* * *   *
* * * *
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if(i==j):
           print(" ",end=" ") 
        else:
            print("*",end=" ")
    print()