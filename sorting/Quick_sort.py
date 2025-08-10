""" Quick sort Algorithem """ 
def quick_sort(list1) : 
    if len(list1) <= 1 : 
        return list1 
    else : 
        pivot = list1[0]   #  pivot is a first element of a list or array 
        lesser = [x for x in list1[1:]  if pivot >= x ]             # we use  slīcing to avoid the first element which is pivot 
        greater = [x for x in list1[1:] if pivot < x ] 
        return  quick_sort(lesser)+[pivot]+quick_sort(greater)      # using recursion 
       
marks = [2,1,34,31,63,62,36,3,623,100,0,64,3,73,4,74] 
print(quick_sort(marks))