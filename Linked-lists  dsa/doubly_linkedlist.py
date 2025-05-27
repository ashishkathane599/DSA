""" DLL ( DOUBLY LINKED LIST )"""   

class node :     # cretating a node for ddl 
    def __init__(self, prev = None , item = None , next = None ): 
        self.prev = next
        self.item = item 
        self.next = next 

class DLL :         # main calss for doubly linked list 
    def __init__(self , start = None ) : 
        self.start = start                 # defining the start node
      
    def is_empty(self) :           # Checking the list is empty of not 
        return self.start is None 

    def insert_at_start(self,data) : 
        n = node(None , data , self.start )     # creating a object of node class
        if not self.is_empty() :  # if list is empty then it will not run becoouse it return (false) and if it is not empty then it will return (true)
            self.start.prev = n   # if thel lilst is not empty then assigning the new node address to the starting node (which will be the secound node )
        self.start = n
    
    def insert_at_last(self,data) : 
        # to find the last node we use traversing 
        temp = self.start      # temp is a local variable which have reference of starting node 
        if self.start != None :       # if list is empty then it will assign None in temp 
             while temp.next is not None :    #  if temp.next is empty then looop will stop (self.start.next is empty then loop will stop )
                temp = temp.next            # it will find the last node of linked list which have next node values None 
        
        n = node(temp,data,None )      # prev = temp (reference of last node 0)  , item = data , next = node (inserting the node at the end )
        
        if  temp == None :    # is list is empty then new node will add at the starting   ( temp = self.start if temp is None then the list is empty )
             self.start =  n 
        else :                 # if list is not empty then new node will add at the ending of the list 
             temp.next = n       # assigning the address of new note to the temp node which is secound last node (previous node of new node n )
    
    """   
---------------------  Traversing -------------------------------------------- 
     1.  before traversing    ( we use traversing after using the if condition ) 
       ex.insert_at_last    function
     2. after traversing      ( we use traversing before if condition ) 
       ex.search function

    """
    
    def search(self,data) :     
        temp = self.start 
        while temp is not None :    # traversing  to find the serched data   
            if temp.item == data :  # if data is found then it retun the node temp 
                return temp    
            temp = temp.next     # for traversing 
        return None                   # if item not found in list the return None 
                 
    
    def insert_after(self,temp,data) : 
        if temp is not None :        #  if temp node is not none then we can add the n.prev = temp   
            n = node(temp,data,temp.next)   #creating new node for inserting after the perticular node 
            if temp.next is not None :   # if it is none then it is present in list 
                temp.next.prev = n       # in temp.next node we assigning the value of new node in the temp.next.prev 
            temp.next = n 
    
    def print_list(self) : 
        temp = self.start 
        while temp is not None : 
            print(temp.item,end =' ')
            temp = temp.next 

    def delete_first(self) : 
        # to delete the node we just ignore the node and changing the addreses remove the first node 
        if self.start is not None :      # if starting node is not none then assigning the addres of secound node to start 
            self.start = self.start.next    # assigning the value of secound node to start (1st considered as a deleted node )
            if self.start is not None :    # secound node is the first node  if there is no secuond node is exist then the condition will bee false 
                self.start.prev = None     # if the secound node exist then add the prev value as a  None in the newly first node which is actually a secound node 
          
    def delete_last(self)  :     
        if self.start == None : 
            pass 
        elif self.start.next is None :  # if there is only one node then the next of the start node is None 
            self.start = None      # to delete that one node we assign the None value to the start 
        else : 
            temp = self.start 
            while temp.next is not None : 
                temp = temp.next         # finding the last node using traversing 
            if temp.prev is not None : 
               temp.prev.next == None      # assigning the None in the secound last node (temp.prev assinging the secound last node and next is use for next of secound last node )

    def delete_item(self,data) : 
        if self.start == None :   # is list is empty then no need to delete a node becouse no nodes are present 
            pass   
        elif self.start.next is None :    # if there is only one node is present 
            if self.start.item == data :  # if the only node have the same value to delete then it will deleted 
                self.start == None 
        else : 
            temp = self.start 
            while temp.next is not None : 
                if temp.item == data :  # finding the deleting element / node 
                    if temp.next is not None :     # if the next node of temp is exist
                       temp.next.prev == temp.prev  # then adding the address of previous node of temp to the prev of temp.next node  
                    if temp.prev is not None :       # if temp.prev is not none then temp is not the first node 
                       temp.prev.next == temp.next   # then assigning the of next node  (temp.prev.next contain the address of next node ) to the previous node  
                    else : 
                        self.start == temp.next      # if the searched node is 1rst node and this is the only node in the list 
                    break 
                temp = temp.next 

    def __iter__(self) : 
        return DLLIterator(self.start) 
class DLLIterator : 
    def __init__(self,start) : 
        self.current = start
    def __iter__(self) : 
        return self 
    def __next__(self):
      if self.current is None:
          raise StopIteration
      data = self.current.item  # Ensure self.current is a Node, not a tuple
      self.current = self.current.next
      return data

    
my_list = DLL() 
my_list.insert_at_start(12)
my_list.insert_after(my_list.search(12),89)
my_list.insert_after(my_list.search(89),90)
my_list.insert_at_last(98) 
my_list.delete_last()
my_list.print_list()

# my_list.insert_after(my_list.search(12),45)
