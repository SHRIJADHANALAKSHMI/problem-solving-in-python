def two_pointer_template(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # do something with arr[left], arr[right]
        if some_condition:
            left += 1
        else:
            right -= 1
    return result