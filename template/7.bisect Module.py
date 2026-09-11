# The Python bisect module provides built-in tools 
# for binary search operations on sorted lists. 
# Its primary purpose is 
# to find the correct insertion point for an element so that 
# the list remains sorted without needing to resort the entire structure.
# Important: Your list must already be sorted before using any bisect function.



from bisect import bisect_left, bisect_right

arr = [1, 3, 3, 5, 7]
bisect_left(arr, 3)   # 1 (leftmost position to insert 3)
bisect_right(arr, 3)  # 3 (rightmost position to insert 3)


import bisect

# The list must be sorted!
numbers = [1, 3, 4, 4, 6]

# Find where to put 4
idx_left = bisect.bisect_left(numbers, 4)   # Returns 2 (before the first 4)
idx_right = bisect.bisect_right(numbers, 4) # Returns 4 (after the last 4)
idx_alias = bisect.bisect(numbers, 4)       # Returns 4 (alias of bisect_right)

print(idx_left)   # Output: 2
print(idx_right)  # Output: 4
