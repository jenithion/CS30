import random, string, copy, time

def get_time_elapsed(function, list, target=None):
    if target == None:
        start = time.time()
        function(list)
        end = time.time()

        ans = end - start
        return ans
    else:
        start = time.time()
        function(list, target)
        end = time.time()

        ans = end - start
        return ans

def gen_random_ints(length, min_val, max_val):
    arr = []
    for i in range(length):
        arr.append(random.randint(min_val, max_val))
    return arr
    
def gen_random_letters(length):
    #Define letters to choose from
    CHARACHTERS = string.ascii_letters
    
    arr = "".join(random.choice(charachters) for i in range(length))
        
    return arr

def get_average(list):
    LIST_LENGTH = len(list)

    total = 0
    for i in list:
        total += i

    ans = total / LIST_LENGTH 
    return ans

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
    
def bubble_sort(list):
    """
    A mutating sort
    Sorts a list in ascending order using bubble sort
    
    Args:
        (list)arr:
        
    return:
        list: sorted list
    """
    #create a copy of the list
    arr = copy.copy(list) 
    #get the length of the array
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
       
def selection_sort(list):
    """
    Prefoms selection sort on a array and returns a sorted array, it is also mutable so it changes the original argument
    
    Args:
        (list) arr: a list
    
    Example:
        mut_selection_sort([5, 3, 8, 4, 2])
        >>> [2, 3, 4, 5, 8]
    
    """
    #create a copy of the list
    arr = copy.copy(list) 
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
    
def insertion_sort(list):
    """
    Prefoms selection sort on a array and returns a sorted array, it is also mutable so it changes the original argument
    
    Args:
        (list) arr: a list
    
    Example:
        mut_selection_sort([5, 3, 8, 4, 2])
        >>> [2, 3, 4, 5, 8]
    """
    #create a copy of list 
    arr = copy.copy(list) 
    #get length of the array
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

def main():
    REPEAT_AMT = 10000 
    LIST_LENGTH = 65545
    TARGET_MIN = 0
    RANDOM_MIN_VAL = -32767
    RANDOM_MAX_VAL = 32767 
    FIX_INDEX = 1
    
    linear_search_times = []
    binary_search_times = []
    bubble_sort_times = []
    selection_sort_times = []
    insertion_sort_times = []

    for reapat in range(REPEAT_AMT):
        random_list = gen_random_ints(LIST_LENGTH, RANDOM_MIN_VAL, RANDOM_MAX_VAL)

        random_target = random.randint(TARGET_MIN, LIST_LENGTH - FIX_INDEX)
        random_list.sort()
        linear_search_times.append( get_time_elapsed( linear_search, random_list, random_list[random_target] ) )
        binary_search_times.append( get_time_elapsed( binary_search, random_list, random_list[random_target] ) )

        bubble_sort_times.append( get_time_elapsed( bubble_sort, random_list ) )
        selection_sort_times.append( get_time_elapsed( selection_sort, random_list ) )
        insertion_sort_times.append( get_time_elapsed( insertion_sort, random_list ) )
        
    linear_search_avg = average(linear_search_times) 
    binary_search_avg = average(binary_search_times)
    bubble_sort_avg = average(bubble_sort)
    selection_sort_avg = average(selection_sort)
    insertion_sort_avg = average(insertion_sort)

    print(linear_search_avg, binary_search_avg, bubble_sort_avg, selection_sort_avg, insertion_sort_avg)

if __name__ == "__main__":
    main()


