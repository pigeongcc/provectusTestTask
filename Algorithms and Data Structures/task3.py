# the solution uses divide-and-conquer approach (binary search)
# this decreases the time complexity of the algorithm from O(n) to O(log n) 

def get_target_index(arr: list, target: int) -> int:
    arr_size = len(arr)

    # considering the border cases separately since bisearch is not capable of
    # "looking" out of array borders
    if target > arr[arr_size-1]:
        return arr_size + 1

    if target < arr[0]:
        return 0

    return binsearch_of_target(arr, 0, arr_size, target)

def binsearch_of_target (arr: list, l: int, r: int, x: int) -> int:
  
    if r >= l:
        mid = l + (r - l) // 2
  
        # if target is at arr[mid]
        if arr[mid] == x:
            return mid
          
        # if target is less than list[mid], then 
        # search it in the left subarray
        elif arr[mid] > x:
            return binsearch_of_target(arr, l, mid-1, x)
  
        # else search it in the right subarray
        else:
            return binsearch_of_target(arr, mid + 1, r, x)
  
    else:
        # if target is not present in the array, then return l
        return l