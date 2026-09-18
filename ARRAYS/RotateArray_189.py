# Step 1: Reverse the entire array
# [7,6,5,4,3,2,1]
# Step 2: Reverse the first k elements

# First 3:

# [7,6,5]

# becomes:

# [5,6,7]

# Array:

# [5,6,7,4,3,2,1]
# Step 3: Reverse the remaining elements

# Remaining:

# [4,3,2,1]

# becomes:

# [1,2,3,4]

# Final:

# [5,6,7,1,2,3,4]

class Solution1:
    def rotate(self, nums, k):

        n = len(nums)

        k = k % n

        # Reverse entire array
        nums.reverse()

        # Reverse first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse remaining elements
        nums[k:] = reversed(nums[k:])

class Solution2:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = [0] * len(nums) #
        for i in range(len(nums)):
            a[(i+k)%len(nums)] = nums[i] #recycle

        for i in range(len(nums)):
            nums[i] = a[i]



#simple solution

# class Solution(object):
#     def rotate(self, nums, k):
#         n=len(nums)
#         rotations = k%n
#         for _ in range(0,rotations):
#             e=nums.pop()
#             nums.insert(0,e)
            
# nums=[1,3,4,5,6]
# k=3
# solution= Solution()
# print(solution.rotate(nums,k))



#anothe rsimple solution
class Solution3(object):
   def rotate(self, nums, k):
       n=len(nums)
       k=n%k
       nums[:]=nums[n-k:] + nums[ :n-k]
       
