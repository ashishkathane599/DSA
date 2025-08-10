"""  Selection sort in python   """
def selection_sort(list1) : 
    n=len(list1) 
    for i in range(n) :   
        min_index = i    #index of smallest value in the list
        for j in range(i+1,n) :   # loop will run till the end get the smallest valur from the list  ( this loop is to find the smalles no )
            if list1[j] < list1[min_index] :
                min_index = j                   # it will give the smallest no in range i+1 , n
        list1[i],list1[min_index] = list1[min_index],list1[i]  # swap it  
    return list1 

l1 = [ 12,14,51,31,4,2,3,42,1] 
sort = selection_sort(l1)
print(sort)
