""" Recursion 
1. recursive function to print first N natural Number """

def Natural_numbers(N) : 
       if N == 0 : 
              return 1 
       Natural_numbers(N-1)
       print(N,end = " ")
Natural_numbers(4)
print()
"""  2. recursive function to print first N natural Number in reverse  """

def Natural_numbers(N) : 
       if N == 0 : 
              return 1 
       print(N,end = " ")
       Natural_numbers(N-1)
    
Natural_numbers(4)
print( )

"""  Write a recrsion function to print first N odd numbers """
def printodd(n) : 
    if n > 0 : 
       printodd(n-1)
       print(2*n-1, end=" ")
printodd(10)
print()

"""write a recrsion function to print first N even numbers """

def printneven(n) : 
    if n > 0 : 
       printneven(n-1)
       print(2*n, end=" ")
printneven(10)
print( )


"""  Write a recrsion function to print first N odd numbers in reverse order  """
def printnoddreverse(n) : 
     if n > 0 : 
        print(2*n-1,end=" ")
        printnoddreverse(n-1)
printnoddreverse(10)
print( )
"""write a recrsion function to print first N even numbers in reverse order """

def printeven_reverse(n) : 
    if n > 0 : 
       print(2*n, end=" ")
       printeven_reverse(n-1)
printeven_reverse(10)
