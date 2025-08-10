""" Priority queue using singly linked list (SLL)"""
    
class Node : 
    def __init__(self,item=None,priority=None,next=None) : 
        self.item = item
        self.priority = priority
        self.next =next 
    
class PriorityQueue : 
    def __init__(self) : 
        self.start = None 
        self.item_count = 0 
    
    def is_empty(self) : 
        return self.start == None 

    def push(self,data,priority) : 
        n = Node(data,priority)  
        if not self.start or priority < self.start.priority :  # the new nodes priority is smallest and self.start is null 
            n.next = self.start   # insert it at the start 
            self.start = n  
        else : 
            temp = self.start   # loop will run till the condition is true if it false then loop stops 
            while temp.next != None and temp.next.priority <= priority : # loop while run till the end and untill the priority of node is less and equal to new node
                temp = temp.next 
            n.next = temp.next 
            temp.next = n 
        self.item_count +=1 

    def pop(self) : 
        if self.is_empty(): 
            raise IndexError("Queue is empty")
        data = self.start.item 
        self.start = self.start.next
        self.item_count-=1  
        return data 

    def size (self) : 
        return self.item_count 

p1= PriorityQueue() 
p1.push("chaityanya",5) 
p1.push("aditya",3)
p1.push("ashish",1)
p1.push("sandya",4)
p1.push("kadam",2)

while not p1.is_empty() : 
   print(p1.pop())