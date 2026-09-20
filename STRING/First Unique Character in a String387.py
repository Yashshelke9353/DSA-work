# Example 1
# Input:
# s = "leetcode"

# Output:
# 0

# Why?

# l → 1 time  ✅
# e → 3 times
# t → 1 time
# c → 1 time
# o → 1 time
# d → 1 time

# The first unique character is:

# l

# Its index is:

# 0


# Example 2
# Input:
# s = "loveleetcode"

# Output:
# 2

# Characters:

# l → 2
# o → 2
# v → 1  ← first unique
# e → 4
# t → 1
# c → 1
# d → 1

# v is at index 2.


# Example 3
# Input:
# s = "aabb"

# Output:
# -1

# Every character appears more than once.


class Solution:
    def firstUniqChar(self, s):
        count={}
        for char in s:
            count[char]=count.get(char,0)+1
            
        for i in range(len(s)):
            if count[s[i]]==1:
                return i
            
        return -1
s="loveleetcode"
solution=Solution()
print(solution.firstUniqChar(s))