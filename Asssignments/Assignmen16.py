""" priority ququq using list """

class priority  : 
    def __init__(self) : 
        self.item = [ ]
        self.item_count = 0  
    
    def is_empty(self) : 
        return self.item_count == 0 
    
    def push (self,data = None ,pre = None ) : 
       if pre != None : 
         self.item.insert(pre,data)
       else : 
          self.item.append(data)
       self.item_count += 1 

    def pop (self) : 
       if self.is_empty() : 
          self.item.pop(0)
        
    def size(self) : 
       return self.item_count 
    
p1 = priority() 
p1.push(12) 
print("size:",p1.size() )
