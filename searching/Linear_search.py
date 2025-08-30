def linear_search(arr,target) : 
    n = len(arr) 
    for i in range(0,n) : 
        if arr[i] == target : 
            return i 
    return -1  

arr = [ 1,2,3,4,5,6,7,8,12,31,42]

result  = linear_search(arr,12)

if result != -1 : 
    print(f"The element found at index: {result}")
else : 
    print("Element not found at any index . ")



