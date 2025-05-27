""" stack data structure by extending list class ( Inheriting list class )
* in this program we use self at the place of list becouse list is the parent class and we use the inheritance here
* while using these method always check the methods or function are present in both the classess or not in child and parent  """

class Stack (list):               # now stack is a subclass of the list class useing inheritance 
        def is_empty(self) : 
              return len(self) == 0 
        
        def push(self,data) : 
               self.append(data)  # stack is a child class of the list so we use self.append other than self.list.append

        def pop(self) : 
                if not self.is_empty() :     # if we call the pop method in this function it will call itself becouse it is present in stack as well as list class 
                    super().pop()            # to stop overridding  we use super() insted of self  (overidding occur when the parent class and child class have the same functions and in child class we call the function then it does not call the parend class function so we use super()
                else :                       # else  raise an epeerror 
                       raise IndexError("Stack is empty.")   
              
        def peek(self) : 
                if not self.is_empty() :    # list is not empty then return the  last data which is entered at a last in the stack 
                      return self[-1]       # using backword indexing -1 is start from the back and from the end of the list 
                else :                      # we use backword indexing becouse we insert values at the end using append function so top value is present at the end of the list            
                    raise IndexError("Stack is empty.")    # if list is empty then return an error 
        
        def size (self) : 
               return len(self) 
        
        # to stop the use of insert method by list we override the insesrt method and create it into the stack class so this method does not call by user means not workable 
        def insert(self) :    # to disable the insert method from the parent class we raise error in child class insert function so user cannot use the insert  method 
               raise AttributeError("No Attribute'insert' in stack ")
        
s1 = Stack() 
s1.push(12)
s1.push(13)
s1.push(14)
s1.pop()
print(s1.peek())
print(s1.size())