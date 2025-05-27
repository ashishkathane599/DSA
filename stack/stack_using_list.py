""" stack using list :- create an empty list in the stack class and create a funcion for the stack operations 
* In stack we use LIFO  (last in first out ) we can only delete the last entered data from the stack """

class stack : 
    def __init__(self) :
        self.item = [ ]       # creating a empty list 

    def is_empty(self):            # to check the stack is empty or not we check the list is empty or not 
        return len(self.item) == 0    # we use the length (len) function if it is 0 then stack is empty 
    
    def push(self,data) :       # push the data into the list  which means we are pushing data into the stack using list 
        self.item.append(data) # we use the append method which is used to add the data at the end of the list 

    def pop(self) :               # In a stack we cannod delete the data according to us deu to the LIFO method 
        if not self.is_empty() :  # we use pop function which is use to delete and return the data at  a time (the last data is deleted using pop function )
            return self.item.pop()          # we are deleting the last data which is inserted first in the stack/list 
        else : 
            raise IndexError("Stack is empty ")   # The raise keyword is used to raise an exception.define what kind of error to raise, and the text to print to the user.
        
    def peek(self) :    # peek function return the top element on the stack 
        if not self.is_empty() :  # negative index worki right to left and start from -1 
          return self.item[-1]   # use negative indexing  to access the last element which is inserted firstly 
        else : 
            raise IndexError("Stack is empty ")
    
    def size(self) : # tell the size of the stack 
            return len(self.item)

s1 = stack() 
s1.push(10)
s1.push(20)
s1.push(30)  
s1.pop()         # it delete 30 becouse it is the last element inserted in the stack 
s1.push(40)
print(s1.peek())
print(s1.size())