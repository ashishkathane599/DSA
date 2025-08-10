# Merge sort  : Divide and conquer
def merge_sort(list) : 
    # base condition 
    if len(list) > 1 : 
        mid = len(list)//2 
        leftlist = list[:mid]       # first half of list
        rightlist = list[mid:]    # secound half of the list 
         
        # regression :- calling the function to divide the list in single single element 
        merge_sort(leftlist) 
        merge_sort(rightlist) 

        # now Merging the divided arrays by sorting 

        i = j = k = 0   # i for left  j for right  and k for original list 
     
        while i < len(leftlist) and j < len(rightlist) : 
            if leftlist[i] < rightlist[j] : 
                list[k] = leftlist[i] 
                i += 1 
            else : 
                list[k] = rightlist[j]     
                j += 1 
            k += 1 
        
        # if any list have remaining elements 
        # for leftlist 
        while i < len(leftlist) :
            list[k] = leftlist[i]
            i += 1 
            k += 1 
         
        while j < len(rightlist) : 
            list[k] = rightlist[j] 
            j += 1 
            k += 1 
    return list 

num = [12,4,23,3,2,45,63,60,42,52]
result = merge_sort(num)
print(result)
