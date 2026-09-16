# class Solution(object):
#     def missingNumber(self, nums):
#         n = len(nums)
#         return n * (n+1) / 2 - sum(nums)
        
        # he varch answer pan chalel leetcode aprove karto
        
        
# class Solution:
#     def missingNumber(self, nums):
#         n = len(nums)

#         expected_sum = n * (n + 1) // 2
#         actual_sum = sum(nums)

#         return expected_sum - actual_sum

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(0, n + 1):
            if i not in nums:
                return i
            
    
nums = [3, 0, 1]   # 
solution = Solution()
result = solution.missingNumber(nums)
print(result)  # Output: 2