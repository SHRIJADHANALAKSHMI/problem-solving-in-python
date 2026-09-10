# Problem 4: Longest Substring Without Repeating Characters ⭐⭐ (very common)

# Find length of longest substring with no repeating characters.
def length_of_longest_substring(s):
    window = set()
    left = 0
    best = 0

    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        best = max(best, right - left + 1)

    return best

print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")