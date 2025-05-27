
""" Dequeu using doubly linked list (DLL)
1. insertion  :-  1. front 2.rear
2. deletion   :-  1. rear 2. front  """

class Node : 
    def __init__(self,item=None,prev = None,next=None) : 
        self.item = item
        self.prev = prev
        self.next = next 

class Deque : 
    def __init__(self,rear=None,front=None) : 
        self.rear = rear
        self.front = front
        self.count = 0 
        
    def is_empty(self) : 
        return self.rear == None 
        # self.front == None 

    def insert_rear(self,data) :  
        n = Node(data)
        if not self.is_empty() : 
            self.rear.next = n  
            n.prev = self.rear
            self.rear = n 
        else : 
            self.rear = n 
            self.front = n 
        self.count += 1 
    
    def insert_front(self,data) : 
        n = Node(data)
        if not self.is_empty() : 
            n.next = self.front
            self.front.prev = n 
            self.front = n 
        else : 
            self.rear = n 
            self.front = n 
        self.count += 1 

    def delete_front(self) : 
        if self.is_empty() : 
            raise IndexError("Deque is empty ")
        else : 
            self.front = self.front.next 
            self.front.prev = None 
        self.count -= 1 
    
    def delete_rear(self) : 
        if self.is_empty() : 
            raise IndexError("Deque is empty ")
        else : 
            self.rear = self.rear.prev 
            self.rear.next = None 
        self.count -= 1 
    
    def get_rear(self) : 
        if not self.is_empty() :  
          return self.rear.item
        else : 
            raise IndexError("Deque is empty ")
        
    def get_front(self) : 
        if not self.is_empty() :  
          return self.front.item
        else : 
            raise IndexError("Deque is empty ")
        
    def size(self) : 
        if not self.is_empty() :  
          return self.count 
        else : 
            raise IndexError("Deque is empty ")
        
d1 = Deque()

d1.insert_front(90) 
d1.insert_rear(100)
d1.insert_rear(40)
d1.insert_front(80) 
d1.insert_front(70)
# d1.delete_front()
# d1.delete_rear()
print(f"Rear : {d1.get_rear()}")
print(f"Front :{d1.get_front()}")
print(f"Size:{d1.size()}")

    