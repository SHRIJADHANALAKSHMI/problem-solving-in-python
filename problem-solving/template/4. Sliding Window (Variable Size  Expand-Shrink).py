def variable_window(s):
    window = set()  # or dict for frequency
    left = 0
    best = 0

    for right in range(len(s)):
        while s[right] in window:   # shrink while invalid
            window.remove(s[left])
            left += 1
        window.add(s[right])       # expand
        best = max(best, right - left + 1)

    return best