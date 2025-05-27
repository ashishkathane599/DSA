"""       SINGLY LINKED LIST        """
class Node : 
    def __init__(self,item=None, next=None ) :  # Local veriable  using to values item store data and next store address
        self.item = item        # Instance object veriable 3 item is local veriable and self.item is instance object veriable 
        self.next = next        # next is local veriable and self.next is instance object veriable  

class SLL :
    def __init__(self,start=None ) : 
        self.start = start
               # start is a local veriable and self.start is instance object veriable it is a starting node 
      
    def is_empty(self) :        # function for checking is list is empty or not 
        return self.next == None   # if next does not contain any value then list is empty (also can write as return self.start == None )
    
    def insert_at_start(self,data) : 
         n = Node(data,self.start)  # n is a object of the Node class and it store the data and address of start node (insertion at the starting)
         self.start = n             # n contain the address of new node and it is assign to the start node 
    
    def insert_at_last(self,data ) : 
        n = Node(data,None)         # creating new node to insert at the last  , therefore the next value is None 
   
        if not self.is_empty()  :
            temp = self.start      # createing a new veriable and assigning the starting node detail 
            while temp.next is not None :    # loop will run until the temp value not become None 
               temp = temp.next            # when the value not become None then it will move to next line (temp.next) and it store in temp 
            temp.next = n           # after finding the last node then adding the new node at the end ( adding the reference of n into temp.next)
        else  : 
            self.start = n              # else list is empty then start node directly contain the new node address .
    
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
             temp.next = n                   # assigning the address of new node to the temp.next   
             
    def print_list(self) : 
        temp = self.start 
        while temp is not None : 
            print(temp.item,end =' ')
            temp = temp.next 
    

    def delete_first(self) :            # deleting the first node 
        if self.start is not None :    # checking the list is not empty 
            self.start =  self.start.next   # assigning the next node address to the start node j

    def delete_last(self) : 
        if self.start is  None :
            pass
        elif self.start.next  is  None : 
            self.start = None 
        else : 
            temp = self.start 
            while temp.next.next is not None :   # finding the secound last node in linked list using (self.next.next ) first next for secound node and last next if to find the last node 
                  temp = temp.next    # It is a secound last Node in linked list 
            temp.next = None     
        
    def delete_item(self,data) : 
        if self.start == None :       # condition one if self.start is empty 
                pass 
        elif self.start.next is None :   # if there is only one node is present 
            if self.start.item == data   : 
                self.start = None
        else :                          # last condition 
            temp = self.start   
            if temp.item == data :
                self.start = temp.next 
            else : 
              while temp.next is not None :     # running the loop until the next values in node is not empty 
                  if temp.next.item == data :       # compairing each node item with the data 
                      temp.next == temp.next.next    # assigning the address of next node of deleted node to the previous node  of deleted node   
                      break 
                  temp = temp.next 
    def __iter__(self) :
        return SLLIterator(self.start) 

    

class SLLIterator : 
    def __init__(self,start) : 
        self.current = start 
    def __iter__(self) : 
        return self 
    def __next__(self) : 
        if not self.current : 
            raise StopIteration
        data = self.current.item 
        self.current = self.current.next 
        return data 

# driver code 
my_list=SLL()
my_list.insert_at_start(10)
my_list.insert_at_start(20) 
my_list.insert_at_start(30) 
my_list.insert_at_start(40)
my_list.insert_after(my_list.search(10),50) 
my_list.insert_after(my_list.search(50),60)
my_list.delete_last()
my_list.print_list( )

print( )
for i in my_list : 
    print(i,end=" ")
