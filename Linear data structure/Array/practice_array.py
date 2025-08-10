# questions 
"""q1.  Write a python script to calculate the average of element . """

from array import * 

arr = array("i" , [12,14,15,16])
list1 = [12,41,51,51]
sum = 0 

# sum of elements in list 
for i in list1 :  # i directly call the index value in list  
      sum += i 
print("sum of the no is :",sum)


# sum of elemet in array 
som = 0 
for x in arr : 
      som += x 
      print("Sum of element in arr: ", som )


# write a python program to creat a list of n odd and even no .
 
even_no = [ ]
odd_no = [ ] 
n = int(input("Enter the range for list : "))
for i in range(n+1) : 
      if i%2 == 0 : 
            even_no.append(i)
      else :
            odd_no.append(i)

print(even_no)
print(odd_no)

l1 = [23,24,252,6]
l1.sort(reverse=True)
print(l1)



