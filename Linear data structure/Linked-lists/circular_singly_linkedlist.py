"""  Circular Linked List  """
class Node : 
    def __init__(self,item=None,next=None) : 
        self.item = item
        self.next = next 

class CLL : 
    def __init__(self,last=None) :   # in circular linked list we  create a last node insted of start node for reducing the traversing time .
        self.last = last
    
    def is_empty(self) : 
        return self.last == None 
    
    def insert_at_start(self,data )    : 
        n = Node(data)   # item = data , next  = None 
        if self.is_empty( ) : 
            n.next = n      # if list is empty then in cll new node will point to itself becouse new node is the last node 
            self.last = n  # last node will point  to itself becouse it is the only node in the list (becouse the new node is first and last node in the list)
        else :
            n.next =  self.last.next  # the new node will point to the first node and first node addresee is saved in the last.next  (cll)
            self.last.next = n    # last node will point to the new node 
    
    def insert_at_last (self,data) : 
        n = Node(data) 
        if self.is_empty() :     
            n.next = n 
            self.last = n 
        else : 
            n.next = self.last.next  # the new node will point to the first node 
            self.last.next = n # last node will point to the new node 
            self.last = n # last node will update the value to the new node now new node is the last node   
        
    def search(self,data) : 
        if self.is_empty( ) : 
            return None 
        temp =  self.last.next  #  temp will point to the first node in cll   ( loop will stop when the last node is equal to temp )
        while temp != self.last :  # if temp is not equal to last node then it will traver the list until the condition is not false
             if temp.item == data :
                 return temp  
             temp = temp.next 
        if temp.item == data :   # this line check the last node becouse the loop will stop when temp is equal to  last node 
            return temp 
        return None 
    
    def insert_after(self,temp,data) : 
        if not self.is_empty() :    # if list is not empty then it will run
            n = Node(data) 
            if temp == self.last :     # if we does not use this condition then the value which are inserted after last node then thes value became first and self.last not point to the last one 
               n.next = temp.next      
               temp.next = n     
               self.last = n 
            else : 
               n.next = temp.next      
               temp.next = n 

    def print_list( self ) : 
        if not self.is_empty( ) : 
          temp = self.last.next 
          while temp != self.last :    # this loop will not print the last node becouse the loop will stop when 
             print(temp.item , end = " " )
             temp = temp.next   
          print(temp.item , end=" ")     # this line will print the last node which is not printed by the while loop     
    
    def delete_first(self) : 
        if not self.is_empty() : 
            if self.last.next == self.last  :  # if there is only one node in the list then we assign none to the last node 
                self.last = None  
            else : 
                self.last.next = self.last.next.next # to delete the first node we assign the last node to the secound node 

    def delete_last(self) : 
        if not self.is_empty() : 
            if self.last.next == self.last : 
                self.last = None 
            else :  
                temp = self.last.next 
                while temp.next != self.last :    # this loop will stop when temp reac to the last node     
                     temp = temp.next    # self.last.next is the first nodes address 
                temp.next = self.last.next # then we assign  the last node to the secound last node and this node point to the first node 
                self.last = temp 

    def delete_item(self,data) : 
        if not self.is_empty() : 
            if self.last.next == self.last :   # address of first node will pointing to the last then it is a only node in list 
                if self.last.item == data : 
                    self.last = None 
            else : 
                if self.last.next.item == data : # checking the first node item is similar to the serched data if there is only one node is present 
                    self.delete_first()   # if item is equal to the data then call the delete_first function 
                else : 
                    temp = self.last.next 
                    while temp != self.last :   # loop will on the privouse node of the founded node
                      if temp.next == self.last :   # when the temp.next is pointed to the last node which is equl to the self.last then next conditions will run 
                          if self.last.item == data : 
                           self.delete_last()     # we will call the function delete_last() 
                          break  
                      if temp.next.item == data :  # when the temp.next node is equal to the data then we will delete the node 
                          temp.next = temp.next.next  # and in previous node of the founded node we will assign the next node of the founded node 
                          break 
                      temp = temp.next

    def __iter__(self) : 
        if self.last == None : 
            return CllIterator(None) 
        else : 
            return CllIterator(self.last.next)

class CllIterator : 
    def __init__(self,start) : 
      self.current = start 
      self.start = start 
      self.count = 0 
    
    def __iter__(self) : 
        return self 
    def __next__ (self): 
      if self.current == None : 
          raise StopIteration 
      if self.current == self.start and self.count ==1 : 
          raise StopIteration 
      else: 
          self.count = 1     
      data = self.current.item 
      self.current = self.current.next
    
      return data 


cll = CLL() 
cll.insert_at_start(20) 
cll.insert_at_start(10)
cll.insert_at_last(30) 
cll.insert_at_last(40)
cll.insert_after(cll.search(40),50)
cll.insert_after(cll.search(50),60)
for x in cll : 
    print(x, end = " ")
print(" ")
 

#  insert after is not working 