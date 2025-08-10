""" Bubble sort using python """
def bubble_sort(data_list): 
    for r in range(1,len(data_list)) : 
         for i in range(len(data_list)-r)  : 
              if data_list[i]>data_list[i+1] : 
                   data_list[i],data_list[i+1] = data_list[i+1],data_list[i] 
    return data_list
l = bubble_sort([53,53,32,5,6,3,64,6,64])
print(l) 