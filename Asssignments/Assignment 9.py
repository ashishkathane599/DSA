""" STACK using sll 
my solution """
class Node : 
    def __init__(self,item=None, next=None ) : 
        self.item = item
        self.next = next

class Stack : 
    def  __init__(self,start=None ) :
         self.start = start
    
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
    
    def pop (self) : 
        if not self.is_empty():
           data = self.start.item   # pop function return the data and delete it  
           self.start = self.start.next
        else : 
            raise IndexError("Stack is empty ")
        
    def peek(self) : 
         if not self.is_empty() : 
              return self.start.item   # the item which is inserted at last it will on the top in the stack 
         else : 
             raise IndexError("Staack is empty ")
         
    def size(self) : 
        if not self.is_empty() : 
            count = 0 
            temp = self.start 
            while temp.next != None :   # and loop will not run for the last node 
                count += 1 
                temp = temp.next 
            return count +1        # loop will stop on the secound last node becouse the next of the last node is emtpy
        else : 
            raise IndexError("stack is empty")
    
s1 = Stack()
s1.push(12) 
s1.push(13)
s1.push(14)
s1.push(15)
s1.pop()
print(s1.size())
print(s1.peek())
