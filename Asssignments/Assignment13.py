""" Queueu using singly linked list """

class Queue : 
    def __init__(self) :
        self.item_count = None 
        self.front = None 
        self.rear  = None 
    
    def is_empty(self ):  
        return self.item_count is None  # rear and front 
    