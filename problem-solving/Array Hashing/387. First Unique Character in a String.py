# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        freq=Counter(s)
        for i,c in enumerate(s):
            if freq[c]==1:
                return i 
        return -1


# efficient solution
class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1