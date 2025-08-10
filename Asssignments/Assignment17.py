"""  priorityqueue  using singly linked list (sll) """

class Node : 
    def __init__(self,item=None,priority=None,next=None) : 
        self.item = item 
        self.priority = priority
        self.next = next

class PriorityQueue : 
    def __init__(self) : 
        self.front = None
        self.rear = None
        self.item_count = 0  
    
    def is_empty(self) : 
        return self.front is None 
    
    def push(self,data,priority) : 
        n = Node(data,priority) 
        if self.is_empty() : 
           self.front = n 
           self.rear = n 
        elif not self.is_empty() : 
            temp = self.front 
            while temp.priority <= n.priority : 
               temp = temp.next 
            n.next = temp.next 
            temp.next = n 
            if temp.next == None : 
               self.rear = n 
        self.item_count += 1 
    
    def get_rear(self) : 
        return self.rear.item
    
    def get_front(self):
        return self.front.item
    
    def pop (self) : 
        if self.is_empty() : 
            raise IndexError("Queue is empty ")
        else : 
            self.front = self.front.next 
        self.item_count -= 1 
    
    def size(self) : 
        return self.item_count 
    
p1 = PriorityQueue() 
p1.push("ashish",5)
p1.push("adity",2)
print(f"rear:{p1.get_rear()} front:{p1.get_front()}")
print(f"size:{p1.size()}")