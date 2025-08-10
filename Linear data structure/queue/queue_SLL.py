""" Queue(FIFO) data strucutre using singly linked list 
* we create a node class and the queue class 
* In queue class we create a functions 1. is empty  2. enqueue  3. dequeue  4. get_rear and get front  5. size
methods : 

insertion          Deletion 
start    ----->    end 
end      ----->   start 
"""
class Node : 
    def __init__(self,item=None,next=None) : 
        self.item = item 
        self.next = next 

class Queue : 
    def __init__(self) : 
        self.item_count = 0 
        self.rear = 0
        self.front  = 0

    def is_empty(self) : 
        return self.rear == 0 
    
    def enqueu(self,data)  : 
        n = Node(data)
        if self.is_empty() : 
            self.front = n 
        else : 
            self.rear.next = n
        self.rear = n    # writing outside the statement beocuse used in both if and else 
        self.item_count += 1      
    
    def dequeue(self) : 
        if not self.is_empty( ) : 
            self.front = self.front.next 
        elif self.front == self.rear : 
            self.front = None 
            self.rear = None 
        else : 
            raise IndexError("Queue overflow ") 
        self.item_count -= 1 

    def get_front(self) : 
        if not self.is_empty()  : 
            return self.front.item
        else : 
            raise IndexError("No data in queue ") 
        
    def get_rear(self) : 
        if not self.is_empty() :
            return self.rear.item 
        else : 
            raise IndexError("No data in queue ") 
            
    def size (self) : 
        return self.item_count 
    
q1 = Queue()
q1.enqueu(30)
q1.enqueu(48) 
q1.enqueu(68) 
print("first:",q1.get_rear())
print("last:" , q1.get_front())
print(q1.size( ))