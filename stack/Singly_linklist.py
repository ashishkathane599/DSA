
class Node : 
    def __init__(self,item = None , next = None ) :
        self.item = item 
        self.next = next 

class SLL : 
    def __init__(self,start=None ) : 
        self.start = start 

    def is_empty(self) : 
        return self.start == None 
    
    def insert_at_first(self,data) :
        n = Node(data,self.start)
        self.start = n 
       
    def insert_at_last(self,data) : 
        n = Node(data,None) 
        if not self.is_empty() : 
            temp = self.start 
            while temp.next is not None : 
                temp = temp.next 
            temp.next = n 
        else : 
            self.start = n 

    def search(self,data) : 
        temp = self.start          # assigning the start node to temp 
        while temp is not None : 
            if temp.item == data :     # checking the data is equal to the serached data 
                return temp       
            temp = temp.next            # if the condition is not satisfied then it will move to next node 
        return None 
    
    def insert_after( self,temp,data ) :  # passing the value of next  node in the temp where we are inserting the new node   
         if temp is not None :               # cheking the temp is not none 
             n = Node(data,temp.next)        # creating the new node and assigning the data and next value of temp.next where the address of next is store after insertion
             temp.next = n         

    def delete_first(self) : 
        if not self.is_empty() : 
          self.start = self.start.next 
        
        
    def delete_last(self)  : 
        if not self.is_empty( ) : 
            if self.start.next == None : 
                self.start = None 
            else :  
              temp = self.start
              while temp.next.next != None : # temp is pointing the secound last node in list becouase temp = self.start.next 
                temp = temp.next 
              temp.next = None 
    
    def print_item(self) : 
        if not self.is_empty() : 
            temp = self.start
            while temp.next != None : 
               print(temp.item,end=" ")
               temp = temp.next 
            print(temp.item,end=" ")


            
# l1 = SLL( )
# l1.insert_at_first(10) 
# l1.insert_at_first(20)
# l1.insert_at_first(30)
# l1.print_item()
