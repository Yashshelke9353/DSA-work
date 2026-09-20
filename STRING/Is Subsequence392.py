# s = "abc"
# t = "ahbgdc"

# We can find:

# a → b → c

# inside t:

# a h b g d c
# ↑   ↑       ↑

# So:

# True


class Solution:
    def isSubsequence(self, s, t):
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
    
s="ash"
t="yash"
#fint s is the subsequence of t or not
solution=Solution()
print(solution.isSubsequence(s,t))