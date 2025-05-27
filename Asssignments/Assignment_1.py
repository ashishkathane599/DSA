"""    Assignment 1  : Array and List    
1. Give an array with some interger type values write a python script to sort the array values . 
"""

# array 
arr = [ 1, 2, 5 ,4 , 7 , 5, 6, 7 , 9 , 10]
arr.sort()
print(arr) 


""" 
2.Give a list of hetrogenous elements . write a python script to remove no interger value from the list .   
"""

values = [ 1, 4,3,4,3,8 ,'j','k', 4, '3', 78, 'a', 'l' , 8, 9 ]

for i in values : 
    if type(i) == str : 
        values.remove(i)
    elif type(i) == int : 
        pass 


""" Write a program to calculate the average of the list elements """

elements = [ 1, 2,3 ,4,5,6,7 ]
average = sum(elements) // len(elements)  # average   = sum of elements / number of elements   
# we use / for decimal value and // for  interger value (non-decimal)
print(average)


# print(2%100==0)
# print(100%2==0)

""" write a python script for creating a list of  the first N prime numbers """
# prim = []
# n = int(input("Enter the value of N : "))
# for i in range(2 , n ) : 
#     count = 1
#     if i % count == 0 and i % count : 
#         prim.append(i) 
#         count =+ 1 
#     else : 
#         count == count 


def prime_num(n) :      # n = range for loops 
    print(" 1 is always a prime no ")
    prime = [1,]
    count = 0
    for i in range(1 , n ) :     # because 1 is prime no so no need to check it for prime no 
        for j in range(1,n) : 
            if i % j == 0 : 
                count += 1 
            else : 
                pass 
        if count == 2 : 
            prime.append(i)
        else : 
            count = 0    # assinging  0 to count variable and making ready for new itteration of i 
    print(prime)
        
prime_num(100)


# solving the same problem using while loop 
""" 
def prime_no ( num ) : 
  print('1 is always a prim no ' )
  i = 1
  count = 0 
  while i < 100 : 
      if num % i == 0 : 
          count += 1
          print(i) 
      else : 
          pass 
      i += 1
      
  if count == 2 : 
    print(num , "is a prime no ")
  else : 
    print(" it is not a prime no ")
prim_no(12)
""" 





""" 
write a python script for creating a list of  the  N terms of the fibonacci series 
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
3 + 2 = 5 
5 + 3 = 8 
8 + 5 = 13
13 + 8 = 21 
21 + 13 = 34 
34 + 21 = 55 

formula : 
f0 + f1 = f2 
f1 + f2 = f3 
f2 + f3 = f4 
""" 
def fibonacci (n) :
   list1 = [0]
   first  = 0   # first no to start the addition of the fibonaccci series 
   secound  = 1   # secount no add with the first 
   i = 1 
   while i < n :    
    ans = first  + secound  #addtion of the no 
    list1.append(ans) 
    first  = secound         # assgining the value fo secound no:s to the fist no : f       to perform : (f0 + f1 = f2 ) 
    secound = ans      # assigning the value of a to s 
    i +=1      # while loop syntax
   print(list1)
    
fibonacci(10)


#  sovlving same problem using recursion 
# this mathod only give a last digint of reange

def fib(n) : 

    if n <= 1 : 
        return n 
    else : 
        return fib(n-1) + fib(n-2) 
        
print(fib(12))