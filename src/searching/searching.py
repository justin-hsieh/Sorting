# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(len(arr)):
        if arr[i] == target:
            return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while low <= high:
        mid = (low + high) // 2
        # If the mid point is the target value, return True
        if target == arr[mid]:
            return mid
        # If target is less than the midpoint, the midpoint becomes
        # the new high point
        elif target < arr[mid]:
            high = mid - 1
        # If the target is larger than the midpoint, the midpoint becomes
        # the new low point
        else:
            low = mid + 1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
