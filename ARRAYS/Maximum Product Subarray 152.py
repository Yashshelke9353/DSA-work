class Solution(object):
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]
        
        for num in nums[1:]:
            old_max = current_max
            old_min = current_min
            
            current_max = max(num,old_max * num, old_min *num)
            current_min = min(num, old_max*num, old_min *num)
            result= max(result, current_max)
            
        return result
    
nums = [2, 3, -2, 4]
solution = Solution()
print(solution.maxProduct(nums)) # Output: 6
