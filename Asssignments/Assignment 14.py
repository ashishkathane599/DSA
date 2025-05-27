"""                 Deque  
deque is a linear data Structure in which Insertion and Deletion occur from both the ends 
Deque is  not Insertion and Deletion Restricted 
* it is a   Double sided queue 

* Queue is  : Insertion and Deletion Restricted 
 1. insertion restricted :- insertion can perform from only one end 
 2. deletion restricted :- deletion can perform from only one end 
"""       
                   # deque using list 

class Deque : 
    def __init__(self) : 
        self.item = [ ]
    
    def is_empty(self) : 
        return len(self.item) == 0 
    
    def insert_front(self,data) : 
        self.item.insert(0,data)

    def insert_rear(self,data) :  
        self.item.append(data)

    def delete_front(self)  : 
        if not self.is_empty() : 
            self.item.pop(0)
        else : 
            raise IndexError("deque is empty ")
    
    def delete_rear(self) : 
        if not self.is_empty() : 
            self.item.pop() 
        else : 
            raise IndexError("Deque is empty ")
    
    def get_front(self) : 
        if self.is_empty() : 
            raise IndexError("Deque is empty ")
        else : 
            return self.item[0]
    
    def get_rear(self) : 
        if self.is_empty() : 
            raise IndexError("Deque is empty")
        else : 
            return self.item[-1]
    
    def size(self) : 
        return len(self.item)
    

q1 = Deque( ) 
q1.insert_rear(19) 
q1.insert_rear(29)
q1.insert_rear(20)      #  leteest inserted value in deque
q1.insert_front(40)
q1.insert_front(90)
q1.insert_front(100)   # oldest value of first value in the deque
# q1.delete_front()
# q1.delete_rear()
print("Rear: ",q1.get_rear())
print("front:",q1.get_front())
print("Size:",q1.size())