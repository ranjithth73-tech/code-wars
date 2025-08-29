def sort_array(arr):
    
    odds = sorted([x for x in arr if x % 2 != 0])
    
    
    result = []
    odd_index = 0
    for num in arr:
        if num % 2 != 0:  
            result.append(odds[odd_index])
            odd_index += 1
        else:  
            result.append(num)
    return result
​
​
​
print(sort_array([7, 1]))                 
print(sort_array([5, 8, 6, 3, 4]))        
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  
​
​