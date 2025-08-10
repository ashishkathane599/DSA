"""   stack by inheriting the singly linked list in python file 
create a stack class as a child class of the SLL class (derived class )"""
from Singly_linklist import *

class Stack(SLL) :  
  def __init__(self) : 
    # self.start is already present in the parent class so it show error when we creat a init method in the child class so we need to call the parent class init function 
    super().__init__(self)   # the self.start is defined in the parent (derived ) so we call the init funccion in child class 
    self.item_count = 0 
    
  def is_empty(self) :   # we cannot call the function directly using self becouse is_empty function is present in both the classes 
    return super().is_empty()  # calling the parent class version 
  
  def push(self,data) :
    self.insert_at_first(data)   # we call it directly  becouse  parent  class does not have the same function of name push 
    self.item_count += 1 

  def pop(self ) : 
    if self.is_empty() == False : 
       self.delete_first()
       self.item_count -= 1 
    else : 
      return None 
  
  def peek(self) : 
    if self.is_empty() == False  : 
      return self.start.item
    else : 
      return None 

  def  size(self) : 
    if not self.is_empty() : 
      return self.item_count
    else : 
      raise IndexError("Stack is empty ")
s1 = Stack()
s1.push(40)
s1.push(30) 
s1.push(20) 
s1.push(10)    # last entered value 
print(f"The top element in the stack is {s1.peek()}")
print(s1.size())

      
""" use of super and self in inheritance (classes )
super( ) : we use a super key when we call the function from the  parent class in the child class(derived class ) 
we call the super function in a case when the both the parent and child have the same function and we want to call the function from the parent class 
otherwise overriding is occure 

self : self key is use to access the function of the same class or from the working classs  """
