""" Binary search treee BST """

class Node : 
    def __init__(self,item= None ,left = None ,right = None ) :  
        self.item = item 
        self.left = left 
        self.right = right 

class BST : 
    def __init__(self,root = None )  : 
        self.root = None
    
    def insert(self,data) : 
        self.root = self.rinsert(self.root,data)
    
    def rinsert(self,root,data) : 
        if root == None :       # when the left of right of the function is empty then the node is created 
            return Node(data) 
        if  root.item > data : 
            root.left = self.rinsert(root.left,data)     # recursivly call the function it check till the root  node is not None 
        
        elif root.item < data : 
            root.left = self.rinsert(root.right,data) 
        return root 
    

    def search(self,data) : 
        return  self.rsearch(self.root,data) 
    
    def rsearch(self,root,data) :  
        if root == None or root.item == data : 
            return root                              # for every search the root node is different 
        if data < root.item : 
            return  self.rsearch(root.left,data)     # for the recursive function root.left now become the root node 
        else : 
            return  self.rsearch(root.right,data)   # for the recursive function root.right become the root node for every recursion 
        
    # traversal 
    def inorder(self) : 
        result = [ ]
        self.rinorder(self.root,result)  
        return result   
    
    def rinorder(self,root,result) :     # left,item,right
      if root :    # if root is not empty 
        self.rinorder(root.left,result) 
        result.append(root.item)
        self.rinorder(root.right,result) 
     

    def preorder(self) : 
        result = [ ]
        self.rpreorder(self.root,result) 
        return result 
    
    def rpreorder(self,root,result)  :    # item , left ,right 
        if root : 
            result.append(root.item) 
            self.rpreorder(root.left,result) 
            self.rpreorder(root.right,result) 

    
    def postorder(self) : 
        result = [ ]
        self.rpostorder(self.root,result) 
        return result 
    
    def rpostorder(self,root,result)  :    # item , left ,right 
        if root : 
            self.rpreorder(root.left,result) 
            self.rpreorder(root.right,result) 
            result.append(root.item) 
        
    def min_value(self,temp):    #  min value from the tree 
        current = temp 
        while current.left is not None : 
            current = current.left 
        return current.item 

    def max_value(self,temp) :  # max value fromm the tree 
        current = temp 
        while current.right is not None : 
            current = current.right 
        return current.item  
        
    def delete(self,data) : 
        self.root = rdelete(self.root,data)

    def rdelete(self,root,data) :
         if root is None : 
             return None 
         if  data < root.item : 
            root.left = self.rdelete(root.left,data)
         elif data > root.item : 
            root.right =  self.rdelete(root.right,data)
         else : 
             if root.left is None : 
                 return root.right 
             elif root.right is None : 
                 return root.left 
             root.item = self.min_value(root.right)       # succesor  :- min value 
             self.rdelete(root.right,root.item)
         return root 
    
    def size(self) : 
        return len(self.inoder()) 


tree = BST() 
tree.insert(45) 
tree.insert(30) 
tree.insert(89) 
tree.insert(42)
tree.insert(50) 

print(tree.preorder()) 
print(tree.inorder()) 
print(tree.postorder())