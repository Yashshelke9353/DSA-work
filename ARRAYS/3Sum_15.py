#aaplyala ek array dila aasel and aamlya ashe 3 integer findout karayche aahet ki jys integer cha sun 0 asel
#yalach 3 sum mhantat
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result
    
    
    
    # nantar understand kRN AAhe aata samazlel ahi