""" queue data structure using list in python  
* queue is a linear data structure in data structure  
*queue is a data structure which is use to store a data
*Working structure of  queue is  FIFO or LILO  (first in first out  or last in last out )  .  
ex. entry and exit of a movie theater in which the first who enetre is exit first and last entered exit at last  
"""

class queue : 
    def __init__(self) : 
        self.item = [ ]

    def is_empty(self) : 
        return len(self.item) == 0 

    def inqueue(self,data) :     # inqueue is use to insert the value into the queue data structure 
        self.item.append(data)   # insert data one after one 

    def dequeue(self) :       # dequeue is use to delete the first inserted data from the queue 
        if not self.is_empty() :   # delete first inserted data from the stack means delete the data from the first index which is 0 
            self.item.pop(0)
        else : 
            raise IndexError("The queue is empty . ")
    
    def get_front(self) : 
        if not self.is_empty() : 
            return self.item[0]    # return the first element in the lists (queue) which is inserted first 
        else : 
            raise IndexError("The queue is empty.")
    
    def get_rear(self) : 
        if self.is_empty() == False :   
            return self.item[-1]   # return the last element from the list (queue )
        else : 
            raise IndexError("The queue is empty ")
    
    def size(self) : 
        if not self.is_empty() : 
            return len(self.item)
        else : 
            raise IndexError("The queue is empty ")
        

q1 = queue( )
q1.inqueue(10)
q1.inqueue(20)
q1.inqueue(30)
q1.inqueue(40)  
print(q1.get_front())
print(q1.get_rear())

print(q1.get_front())
print(q1.size())


# complete 