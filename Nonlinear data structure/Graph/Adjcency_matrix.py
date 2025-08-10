# implimentation of adjcency matrix graph 

class Graph : 
    def __init__(self,vno) :  # vno :- vertex count or node count 
        self.vertex_count = vno   # * : repetation oprator becouse we multipying list with int 
        self.adj_matrix = [[0]*vno for e in range(vno)]    # list comprihension is used to create a matrix of size vno 

    def add_edge(self,u,v,weight = 1 ) :  # u and v are the strating vertex and ending vertex simultaneusly  
        if 0<=u<self.vertex_count and 0 <=v<self.vertex_count:
             self.adj_matrix[u][v] = weight 
             self.adj_matrix[v][u] = weight
        else : 
            print("Invalid vertex") 
        
    def remove_edge(self,u,v) : 
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = 0 
            self.adj_matrix[u][v] = 0 
        else : 
            print("Invalid vertex")
    
    def hash_edge(self,u,v) : 
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!= 0 
        else : 
            print("Invalid vertex ")
    
    def print_edj_matrix(self) : 
        for row_list in self.adj_matrix : 
             map(str,row_list)   # map converrt each element into string and pass a list 
             print(" ".join(map(str,row_list)))  # it remove the " " and provide a list list without " " 

    
g1 = Graph(5) 
g1.add_edge(1,3,12)
g1.add_edge(0,2,81)
g1.add_edge(4,4,10)
g1.print_edj_matrix()
g1.remove_edge(4,4)
g1.print_edj_matrix() 