#check karaich aste ki eka string madhe words dusrya string maddhe purn aahe ki nahi
#rearange kaelyanantar pan same lettersa present pahije
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t) 
    
    #sort karel both string and check karel ki match  hota aaahe ki nahi 
        # s = "listen"
        # sorted(s) = "eilnst"
        # t = "silent"
        # sorted(t) = "eilnst"
    
s="anagram"
t="nagaram"
solution=Solution()
print(solution.isAnagram(s,t))