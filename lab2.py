#!/usr/bin/env python
# coding: utf-8

# In[18]:


import string
import numpy as np
import matplotlib.pyplot as plt
import copy
class Point:
    """ Point Class """
 
    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord
 
    @classmethod
    def input_point(point):
        """ Takes X-Coord and Y-Coord from user to form a point """
        return point(
            int(input('  X-Coord: ')),
            int(input('  Y-Coord: ')),
        )
 
    def __str__(self):
        """ Displays point's coordinates """
        return "(" + str(self.x) + ", " + str(self.y) + ")"
 

 
def dir(A,B,P):
    #print(A,B,P)
    c=copy.deepcopy(B)
    d=copy.deepcopy(P)
    c.x -= A.x 
    c.y -= A.y 
    d.x -= A.x 
    d.y -= A.y 
    #print(c,d)
    ' Determining cross Product '
    cross_product = c.x * d.y - c.y * d.x  
    #print(cross_product)
    if (cross_product > 0): 
        return 1
    elif (cross_product < 0): 
        return -1
    else:
        return 0

def Checkintersection(A,B,C,D):
    #print(A,B,C,D)
    if (dir(A,B,C)==0):
            #print(dir(A,B,C))
            #print(A,B,C)
            if ((A.x<=C.x and C.x<=B.x)and (A.y<=C.y and C.y<=B.y)):
                print("Line Segments",A,B,"and",C,D,"intersect improper intersection")
            elif (dir(A,B,D)==0 and D.x>=A.x):
                print("Line Segments",A,B,"and",C,D,"intersect improper intersection")
            else:
                print("Line Segments",A,B,"and",C,D,"donot intersect ")
                
    elif (dir(A,B,D)==0):
            if ((A.x<=D.x and D.x<=B.x)and (A.y<=D.y and D.y<=B.y)):
                print("Line Segments",A,B,"and",C,D,"intersect improper intersection")
            else:
                print("Line Segments",A,B,"and",C,D,"donot intersect ")
    
                
    elif ((dir(A,B,C)!=dir(A,B,D)) and (dir(C,D,A)!=dir(C,D,B))):
        print("1 Line Segments",A,B,"and",C,D,"intersect proper intersection")
        
    elif (dir(A,B,C)==dir(A,B,D)):
        print("Line Segments",A,B,"and",C,D,"donot intersect ")
        
    else:
        print("none")
        
def directionOfPoint(A,B,P):
    c=copy.deepcopy(B)
    c.x -= A.x 
    c.y -= A.y 
    P.x -= A.x 
    P.y -= A.y 
    #print(c,P)
    ' Determining cross Product '
    cross_product = c.x * P.y - c.y * P.x    
    if (cross_product > 0): 
        print("left turn so area is positive\t",cross_product/2,"\twith line segment",A,B)
    elif (cross_product < 0): 
        print("right turn so area is negative\t",cross_product/2,"\twith line segment",A,B)
    else:
        print("colinear area\t",cross_product/2,"\twith line segment",A,B)
           


# In[19]:


infile=open('linepoint.txt', 'r')
cord = infile.read().split(' ')
cord = list(map(int, cord))
print(cord)
start_point=Point(cord[0],cord[1])
terminal_point=Point(cord[2],cord[3])
i=4
while i in range (4,len(cord)):
        print("\nEnter Query Point")
        query_point = Point(cord[i],cord[i+1])
        print(start_point, terminal_point, query_point)
        directionOfPoint(start_point, terminal_point, query_point)
        i=i+2


# In[20]:


infile=open('lineline.txt', 'r')
cord = infile.read().split(' ')
cord = list(map(int, cord))
print(cord)
start_point1=Point(cord[0],cord[1])
terminal_point1=Point(cord[2],cord[3])
i=4
while i in range(4,len(cord)):
        print(i)
        start_point2 = Point(cord[i],cord[i+1])
        terminal_point2 = Point(cord[i+2],cord[i+3])
        X=copy.deepcopy(start_point1)
        Y=copy.deepcopy(terminal_point1)
        #print(X,Y,start_point2,terminal_point2)
        Checkintersection(X,Y,start_point2,terminal_point2)
        i=i+4
        
    
print("\nDONE.\n")


# In[ ]:





# In[ ]:





# In[ ]:




