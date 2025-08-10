#Array in python
"""
1. Array is a linear data type in python
2. Array is no inbuld in python 
3. To use array we wan't to import array 
4. Array is compact and store a same type of data 
"""

#syntax 
from array import * 
a1 = array("i",[12,42,25,36,38])

# Traversal operation 
for i in range (5) :
    print( a1[i])

for i in a1 : 
  print(i , end = " ")

# Append 
a1.append(14)
print(a1)


# Remove 
a1.remove(42)
print(a1)

# update 
a1[0] = 13
print(a1)
