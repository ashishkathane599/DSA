""" Modified bubble sort in python """
def modified_bubble_sort(data_list) : 
    flag = False 
    for r in range(1,len(data_list)) :  # loop for rounds  round :- len-1 
        flag = False          
        for i in range(len(data_list)-r) : 
            if data_list[i] > data_list[i+1] : 
                data_list[i],data_list[i+1] = data_list[i+1],data_list[i] 
                flag = True
        if not flag  : 
            break 
    return data_list

        
list1 = [34,53,32,62,353,43]
l1=modified_bubble_sort(list1) 
print(l1)   