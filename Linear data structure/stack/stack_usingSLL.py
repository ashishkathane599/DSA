""" STACK using sll 
insertion           Deletion 
start    ------->  End 
End      ------->  Start 
Mysirg solution 
"""
class Node : 
    def __init__(self,item=None, next=None ) : 
        self.item = item
        self.next = next

class Stack : 
    def  __init__(self,start=None ) :
         self.start = start
         self.item_count = 0
    
    def is_empty(self) : 
        return self.start == None 
    
    def push(self,data) : 
        if not self.is_empty( ) :
            n = Node(data)
            n.next = self.start  # before creating the new node self.start pointing to the first node 
            self.start = n 
        else : 
            n = Node(data)
            self.start = n 
            n.next == None  #  next value should be by default None 
        self.item_count += 1 
    
    def pop (self) : 
        if not self.is_empty():
           data = self.start.item   # pop function return the data and delete it  so we create a new veriable to return 
           self.start = self.start.next
           self.item_count -= 1  
           return data
        else : 
            raise IndexError("Stack is empty ")
        
        
    def peek(self) : 
         if not self.is_empty() : 
              return self.start.item   # the item which is inserted at last it will on the top in the stack 
         else : 
             raise IndexError("Staack is empty ")
         
    def size(self) : 
        return self.item_count 
    
s1 = Stack()
s1.push(12) 
s1.push(13)
s1.push(14)
s1.push(15)
s1.pop()
print(s1.size())
print(s1.peek())
