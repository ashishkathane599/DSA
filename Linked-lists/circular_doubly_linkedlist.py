"""CIRCULAR DOUBLY LINKED LIST   (  CDLL )"""

class Node : 
    def __init__(self,item=None,prev=None,next=None) :  # always insert item at first becouse we always provide a item in object and prev next should be None some times 
        self.prev = prev 
        self.item = item 
        self.next = next 

class CDLL : 
    def __init__(self,start=None) : 
        self.start = start

    def is_empty(self) : 
        return self.start == None   
          
    
    def insert_at_start (self,data) : 
        n = Node(data)              # creating new node 
        if not self.is_empty()  :   # checking if linked list is empty or not if empty then run the if statement 
            n.prev = self.start.prev   # assigning the prev to the new node  which is stored in the start.prev
            n.next = self.start        # assigning next to the new node 
            self.start.prev.next = n   # this code assign the add of new node to the last node 
            self.start.prev = n        # assinging new node add to the secound node              
        else :              # if there is no node means n is the only node 
            n.next = n                
            n.prev = n 
        self.start = n  # changing the value of the self.start = n 
    
    def insert_at_last(self,data) :
        n = Node(data)     # prev and next is none untile we assign the value to them 
        if not self.is_empty() : 
            n.prev = self.start.prev # assigning the last node add to the new last node 
            n.next = self.start      # assigning next to the new node which point to the first node of the linked list 
            n.prev.next = n # changing the last node next and assigning the new node to the next of the last node 
            self.start.prev = n      # updating the first node and assing the new node to the prev of the first node 
        else : 
            # if it is empty then 
            n.next = n     
            n.prev = n 
            self.start = n   # if list is empty then n is the only node which is the first and the last node itself

    def search(self,data) : 
        temp = self.start 
        if self.is_empty() : 
                return None 
        if temp.item == data :   # if data is present in the first node then  it return the first node 
             return temp 
        else:                     # if data is not present in the first node then we assign the next node add to the temp 
             temp = temp.next  
       
        while temp != self.start  :   # when temp  value is equal to the last node then it will stop 
                if temp.item == data : 
                     return temp 
                temp = temp.next 
        return None 
            

    def insert_after (self,temp,data) :    # we use temp directly because when we call the function directly then we also call the seacrh function inside the insert func
                                           # temp if there for the searched value 
        if temp is not None :     
            n = Node(data )         # if temp.item is equal to the searched data then following code will run 
            n.prev = temp 
            n.next = temp.next 
            temp.next.prev = n       # assigning the add of the new node to the next node of the new node 
            temp.next = n            # assigning the add of the new node to the previous node of the new node 

    def print_list(self) : 
         if not self.is_empty() :  # Traversing to print the data in each node 
              temp = self.start
              if temp is not None : 
                   print(temp.item, end = " ")
                   temp = temp.next
              while temp != self.start :   # if self.start is equl to the last node then the loop will stop itteration 
                   print(temp.item,end=" ")     # printing the each item of the each iteration in every node 
                   temp = temp.next             # increasing the temp value 
           
    def delete_first(self) : 
        if not self.is_empty() : 
          if self.start.next == self.start :   # if there is only one node is present then self.start= none 
              self.start = None 
          else : 
              self.start.prev.next = self.start.next 
              self.start.next.prev = self.start.prev
              self.start = self.start.next 
        
    def delete_last(self) :
        if not self.is_empty() :  
          if self.start.next == self.start :    # if there is only one node is present then self.start = none 
              self.start = None
          else : 
              self.start.prev.prev.next = self.start 
              self.start.prev = self.start.prev.prev 
       
    def delete_item(self,data) : 
        if not self.is_empty() : 
            temp = self.start
            if temp.item == data :  # checking the item is present on the first node or note 
                self.delete_first()  # if the item is present at the first node then call the delete_first function 
            else :                  
                temp = temp.next       # if item not present at the first node then temp assign the next node (temp.next )
                while temp is not self.start  :   # traversing  when temp == self.start then the loop will stop 
                    if temp.item == data :       # if temp.item found the data then the if condition stat running 
                        temp.prev.next = temp.next 
                        temp.next.prev = temp.prev 
                    temp = temp.next 

    def __iter__(self) : 
        return CDDLLIterator(self.start)
    
class CDDLLIterator : 
    def __init(self,start) : 
        self.current=start
        self.start = start 
        self.count=0
    def __iter__(self) :
        return self
    def __next__(self) : 
        if self.current is None : 
            raise StopIteration 
        if self.current == self.start and self.count==1 : 
            raise StopIteration
        else : 
            self.count = 1 
        data = self.current.item 
        self.current.current.next 
        return data 
              
              
          
         
    
list1 = CDLL()  
list1.insert_at_start(10)
list1.insert_at_last(90)
list1.insert_after(list1.search(10),20)
list1.insert_after(list1.search(20),30)
list1.insert_after(list1.search(30),40)
list1.delete_item(90) 
list1.insert_at_last(50)
list1.print_list()

