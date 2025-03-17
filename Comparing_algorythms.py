import random, string, copy, time

def time_elapsed(function *args):
    start = time.time()
    function(args)
    end = time.time
    return end - start

def random_list(length, max_val, min_val):
    arr = []
    for i in range(length):
        arr.append(random.randint(min_val, max_val))
    return arr
    
def random_letters(length):
    #Define letters to choose from
    charachters = string.ascii_letters
    
    
    arr = "".join(random.choice(charachters) for i in range(length))
        
    return arr

def linear_search(arr, target):
    """
    Preforms a linear serach on a sorted or unsoreted list
    
    Args:
        arr(list): a list of nums
        target(int or float): the value to search for

    Example:
        linear_search([range(1, 10)], 6)
        >>> 5
        
        linear_search([range(1, 10, 2)], 4)
        >>> -1
    """
    for value in range(len(arr)):
        if arr[value] == target:
            return value
    return -1
            
def binary_search(arr, target):
    """
    Preforms Binary search on a sorted list
    
    Args:
        arr(list): a sorted list of nums
        target(int or float): the value to search for

    Example:
        binary_search([range(1, 10)], 6)
        >>> 5
        
        binary_search([range(1, 10, 2)], 4)
        >>> -1
    """
    
    low = 0
    high = len(arr) - 1
    mid = 0
    
    i = 0
    while low <= high:
        mid = (high + low) // 2 #find mid point through average
        
        #if target is equal to the middle elemtnt
        if arr[mid] == target:
            return mid
        #if target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        #if target is smaller, ignore right side
        else:
            high = mid - 1
            
    #target not found
    return -1
    
def mut_bubble_sort(arr):
    """
    A mutating sort
    Sorts a list in ascending order using bubble sort
    
    Args:
        (list)arr:
        
    return:
        list: sorted list
    """
    n = len(arr)
    
    #list empty edge case
    if n <= 1:
        return arr
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
        #n is total nums, i is the num of passes completed, subract 1 so we do not compare sorted elements at the end
            if arr[j] > arr[j + 1]:
                #swap the varible indexs
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break
    
    return arr
       
def mut_selection_sort(arr):
    """
    Prefoms selection sort on a array and returns a sorted array, it is also mutable so it changes the original argument
    
    Args:
        (list) arr: a list
    
    Example:
        mut_selection_sort([5, 3, 8, 4, 2])
        >>> [2, 3, 4, 5, 8]
    
    """
    # get length of array
    n = len(arr) 
    
    #list empty edge case
    if n <= 1:
        return arr

    #iterate through the whole array excluding the final element
    #due to the final element being sorted after checking all other elements
    for i in range(n - 1):  
        #initialize the min_idx and assume its the start of the array
        min_idx = i         
         #iterate through the non sorted part of the array to find min_idx
        for j in range(i + 1, n):  
            #find the min_idx
            #if the item at the current min_idx is greater thatn that of the current item the min_idx will equal the current idx
            if arr[j] < arr[min_idx]: 
                min_idx = j
                
        #swap the item of the min_idx with the start of the unsorted part of the array    
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
        
    return arr
    
def mut_insertion_sort(arr):
    """
    Prefoms selection sort on a array and returns a sorted array, it is also mutable so it changes the original argument
    
    Args:
        (list) arr: a list
    
    Example:
        mut_selection_sort([5, 3, 8, 4, 2])
        >>> [2, 3, 4, 5, 8]
    """
    
    n = len(arr)
    
    #list empty edge case
    if n <= 1:
        return arr
        
    for i in range(1, n):
        #key is the current selected element that needs to be sorted
        key = arr[i]
        #j is the start of the sorted part of the array
        j = i - 1
        
        #shift all items in the sorted part of the array to the right(arr[current_idx++]) until the key is in the correct place
        #we use j >= 0 to ensure that the key doesnt go past the start of the array due to python's negitive elements
        while (j >= 0) and (key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j+1] = key
        
    return arr
    
arr2 = [5, 3, 8, 4, 2]

assert linear_search(arr, 7) == 3
assert binary_search(arr, 7 ) == 3
