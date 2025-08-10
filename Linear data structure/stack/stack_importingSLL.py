""" stack using importing SLL (singly linked list ) Module 
create a object of the SLL in stack """
from Singly_linklist import * 

class Stack : 
    def __init__(self) : 
        self.item = SLL()  # object of the singly linked list class 
        self.item_count = 0 
        # before accesing the function from the class SLL we use self.item.fun_name 
    
    def is_empty(self): 
       self.item.is_empty()
       
    def push(self,data) : 
        self.item.insert_at_first(data)      
        self.item_count += 1   
    
    def pop(self) :
      if not self.is_empty() : 
        self.item.delete_first() 
        self.item_count -= 1  
      else : 
          raise IndexError("Stack is empty.")
    
    def peek(self) : 
       if not self.is_empty() :    
          return self.item.start.item 
       else : 
          raise IndexError("stack is empty")
       
    def size (self) : 
       return self.item_count
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print(s1.size())