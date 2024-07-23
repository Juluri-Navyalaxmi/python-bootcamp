#problem 3

''' mr z is participating in swimming competition 
only 1 winner is selected from all participents and mr x and mr y ae friends of z 
,mr x is participating in badmention,mr y in tabletennies
according to selection comitte requirment for badmintor players are
                                                                   1.height-> 140cm
                                                                   2.weight-> factor of 2
                                                                   3.bodyfat-> less than 12%
                                          for tabletennies players are
                                                                       1.height-> 118cm to 148cm
                                                                       2.weight-> number of medals won by mr z 
                                                                       3.bodyfat-> 14%  
according previous history z participated in 14 games out of which he is having sucess rate of 65% 
now write a program to check weather mr x,mr y,mr z from india travels in same plane or not .  '''


height_x=int(input("enter height"))
weight_x=int(input("enter weight"))
height_y=int(input("enter height"))
medals_won_by_z=14*0.50
weight_y=medals_won_by_z
#condition for qualification
#x conditions
x_qualifies=height_x >= 140 and weight_x % 2 ==  0
#y conditions
y_qualifies= 118<= height_y <= 148 and weight_y ==  medals_won_by_z
if x_qualifies and y_qualifies:
    print("mr.x,mr.y,mr.z can travel in a same plane")
else:
   print("they cant travel in same plane") 

