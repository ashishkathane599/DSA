""" REcursion questions """ 

" 1.  Write a recursive function to calculate a sum of first N natural  Numbers . "
def Natural_numbers(N) : 
       if N == 0 :    # base case 
              return 0 
       return N + Natural_numbers(N-1)    # recursive case 
print("sum of natural:",Natural_numbers(4))
print( )

"""2. Write a recursiove functionto calculate a sum of first N odd numbers """ 

def Sum_odd(n) : 
    if n==0 : 
        return 0
    return 2*n-1+ Sum_odd(n-1)
print("sum odd :",Sum_odd(5))

"""2. Write a recursiove functionto calculate a sum of first N even numbers """ 

def Sum_even(n) : 
    if n==0 : 
        return 2
    return 2*n + Sum_even(n-1)
print("sum even :",Sum_even(5))


""" Factorial of first N numbers """
def factorial(n) : 
     if n == 1 : 
          return 1 
     return n * factorial(n-1) 

print("Factorial : " ,factorial(10))
print()

""" Write a recursive function to calculate sum of first n squars """ 

def Squar_sum(n) : 
     if n == 0 : 
          return 0
     return (n*n) + Squar_sum(n-1)

print("sum_squar:",Squar_sum(10))