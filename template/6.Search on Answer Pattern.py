def search_on_answer(lo, hi, is_valid):
    while lo < hi:
        mid = (lo + hi) // 2
        if is_valid(mid):
            hi = mid          # mid works, try smaller
        else:
            lo = mid + 1       # mid doesn't work, need bigger
    return lo