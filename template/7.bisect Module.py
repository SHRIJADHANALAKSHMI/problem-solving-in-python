from bisect import bisect_left, bisect_right

arr = [1, 3, 3, 5, 7]
bisect_left(arr, 3)   # 1 (leftmost position to insert 3)
bisect_right(arr, 3)  # 3 (rightmost position to insert 3)