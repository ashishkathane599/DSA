""" practice questions """
""" 1. recursive function to print first N natural Number """

def printn(n) : 
    if n > 0 : 
        printn(n-1)
        print(n,end=" ")
        print()
printn(10)
print()
""" 2. recursive function to print first N natural Number """

def printn(n) : 
    if n > 0 : 
        print(n,"\n") 
        printn(n-1)
printn(10)
print()

"""  Write a recrsion function to print first N odd numbers """
def printnodd(n) : 
     if n > 0 : 
        printnodd(n-1)
        print(2*n-1,end=" ")
printnodd(10)
print()

"""write a recrsion function to print first N even numbers """

def printeven(n) : 
    if n > 0 : 
       printeven(n-1)
       print(2*n, end=" ")
printeven(10)
print( )

"""  Write a recrsion function to print first N odd numbers in reverse order  """
def printnoddreverse(n) : 
     if n > 0 : 
        print(2*n-1,end=" ")
        printnoddreverse(n-1)
printnoddreverse(10)
print()

"""write a recrsion function to print first N even numbers in reverse order """

def printeven_reverse(n) : 
    if n > 0 : 
       printeven_reverse(n-1)
       print(2*n, end=" ")
printeven_reverse(10)



#     More questions 