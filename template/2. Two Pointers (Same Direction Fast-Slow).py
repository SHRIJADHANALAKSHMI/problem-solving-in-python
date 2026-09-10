def fast_slow_template(arr):
    slow = 0
    for fast in range(len(arr)):
        if condition:
            arr[slow] = arr[fast]
            slow += 1
    return slow