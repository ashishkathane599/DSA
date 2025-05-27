# Array in python
# ".py "is the module in the python 

from array import *
a1 = array ("i" , [ 1,23,31,1,15,6] )
     # array ( "type cast" , [data elemets] )
     
print(a1)

#Traversal operation 
print(type(a1)) 
for i in range (5) :   # loops using indexing for searching
    print( a1[i] , end = " ") 

for i in a1 :
    print("\n",i, end = " " )


# Operations on array
"""
    1.update
    2.Traversal
    3.remove
    4.sort
    5.append
    6.update
"""

# Sorting array

"""
array.sort() = True
array.sort(reverse) = True 
"""
l1 = [44,3,5,35]
