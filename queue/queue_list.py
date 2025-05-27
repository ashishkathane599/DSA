""" queue data structure useing list in python 
1. inqueue  (reare)  
2. dequeue  (front)
"""
class Queue : 
    def __init__(self) : 
        self.item = [ ] 

    def is_empty(self) : 
        return len(self.item) == 0 
    
    def enqueue(self,data) : 
        self.item.append(data)
    
    def dequeue(self) : 
        if not self.is_empty() : 
            self.item.pop(0)
        else : 
            raise IndexError("Queue Unerflow")
    
    def get_front(self) :
        if not self.is_empty() :  
            return  self.item[0]
        else : 
            raise IndexError("Queue Underflow ")
       
    def get_rear(self) : 
        if not self.is_empty() : 
            return self.item[-1]
        else : 
            raise IndexError("Queue Underflow ")
    
    def size(self) : 
        if not self.is_empty() : 
            return len(self.item) 
    
q1 = Queue()
q1.enqueue(12) 
q1.enqueue(14) 
q1.enqueue(13) 
q1.enqueue(15) 
q1.enqueue(17) 
q1.enqueue(18) 
q1.dequeue()
print("The new inserted values:", q1.get_rear())
print("The oldest values :",q1.get_front())