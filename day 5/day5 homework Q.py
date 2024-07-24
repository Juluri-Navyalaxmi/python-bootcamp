#print upper triangular matrix
#print lower
#print rhombus
#print parlogram 
'''
***
 ***
  *** '''
#upper
'''
for i in range(5):
    for j in range(5):
        if(i==j or i<j):
            print("*",end="")
    print() '''

#lower
for i in range(5):
    for j in range(5):
        if(i==j or i>j):
            print("*",end="")
    print() 




# for i in range(n):                      #   #   #   #    
#     for j in range(n):               #  #   #   #   #
#         if i==j:                     #
#             print("$",end="")
#         else:
#             print("*",end=" ")   
#     print()  




'''
    
    ''''print rhombus'''

# n=int(input()) 
# for i in range(n):                                        #
#     print(" "*(n-i-1),end=" ")                          #   #   
#     for j in range(i):                                #   #   #   
#         print("*",end=" ")                          #   #   #   #   
#     print()                                           #   #   #   
# for i in range(n-1,0,-1):                               #   # 
#     print(" "*(n-i),end=" ")                              #
#     for j in range(i-1,0,-1):
#         print("*",end=" ")
#     print()


'''4)###
       ###
         ### print'''
# n=int(input())                                  # # # #
# k=0                                               # # # #
# for i in range(1,n+1):                              # # # #
#     print(" "(k),""*n)                              # # # #
#     k+=1                                            
#     if k>n:
#         break


# '''5)print number peromid'''                         1
# n=int(input())                                      2 2
# for i in range(1,n+1):                             3 3 3
#     print(" "*(n-i),end="")                       4 4 4 4
#     for j in range(1,i+1):                       5 5 5 5 5
#         print(i,end=" ")
# print()   


# n=int(input())                            # # # # # # # # #
# for i in range(n):                          # # # # # # #
#     for j in range(i+1):                      # # # # #
#         print(" ",end=" ")                      # # #
#     for j in range(i,n):                          #
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()      




# n=int(input()) 
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i-1):                          # # # # # # #
#         print("*",end=" ")                      # # # # # # # # #
#     print()