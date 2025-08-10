""" Queueu data structure by inheriting list as a class and queue is a child class of the list class
not creating any object or a list to perform the Queue

by inheriting list class ( Inheritance concept is used ) """

class Queue(list) :   
        # self = self act as a list in the program "every functioṇ and methods of list are used with a self as a list "
    def is_empty(self) : 
        return len(self) == 0  
    
    def enqueue(self,data) : 
        self.append(data)       # using append with a self becouse self refers to the list 

    def dequeue(self) : 
        if not self.is_empty() :      
            self.pop(0)         # using self as list so using pop method with the self
        else : 
            raise IndexError("Queue overflow ")
    
    def get_rear(self) : 
        if not self.is_empty() : 
            return self[-1]         # using indexing with the self becose self = list 
        else : 
            raise IndexError("Queue overflow")
    
    def get_front(self) : 
        if not self.is_empty() : 
            return self[0] 
        else : 
            raise IndexError("Queue overflow")
    
    def size(self) : 
        return len(self) 

q1 = Queue() 
q1.enqueue(12) 
q1.enqueue(13) 
q1.enqueue(14) 
q1.enqueue(15)
q1.dequeue()
print(f"The latest element : {q1.get_rear()}")
print(f"The oldest element : {q1.get_front()}")

    