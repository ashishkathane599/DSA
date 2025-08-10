""" priority queue using list
priority :-  small Number -> more priority for this program
              1    ->  first priority  """

class priorityQueue : 
   def __init__(self) : 
        self.item = [ ]
    
   def is_empty(self) : 
      return  len(self.item) == 0 
    
   def push (self,data = None ,priority = None ) :  # using touples in list to store data and priority 
      index = 0    # small priority come first        
      while index < len(self.item) and self.item [index][1] <= priority :   # first condition check the list is empty or not 
         index += 1           # secound condition check priority value from the touple ( data,priority) (34,2) || (0 , 1) = index
      self.item.insert(index,(data,priority))   # inserting touple in the list 

   def pop (self) : 
      if not self.is_empty() :    # deleting hightest priority 
         return self.item.pop(0)[0]  # squar bracket is use for indexing to return the pop data 
     
      else : 
         raise IndexError ("Queue is empty")
        
   def size(self) : 
      return len(self.item) 
    
p1 = priorityQueue() 
p1.push("chaityanya",5) 
p1.push("aditya",3)
p1.push("ashish",1)
p1.push("sandya",4)
p1.push("kadam",2)

while not p1.is_empty() : 
   print(p1.pop())