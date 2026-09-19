class Solution:
    def isPalindrome(self, s):

        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:

            if not s[left].isalnum():#ignore the puncutation and spaces
                left += 1
                continue

            if not s[right].isalnum(): #this
                right -= 1
                continue

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
    
    
    
# class Solution(object):
#     def isPalindrome(self, s):
#         r=len(s)//2 #this gives
#         for i in range(r):
#             if s[i] != s[-(i+1)]:
#                 return False
#         return True
# s="madam"
# solution=Solution()
# print(solution.isPalindrome(s))

#for interview only