class Solution:

    def twoSum(self, nums, target):

        # Dictionary मध्ये number आणि त्याचा index store करू
        seen = {}

        # प्रत्येक number check करू
        for i in range(len(nums)):

            # Current number
            num = nums[i]

            # आपल्याला कोणता number हवा आहे ते find करा
            needed = target - num

            # Required number आधी पाहिला आहे का?
            if needed in seen:

                # होय, म्हणून दोन्ही indexes return करा
                return [seen[needed], i]

            # Current number आणि त्याचा index dictionary मध्ये store करा
            seen[num] = i

        # जर pair मिळाला नाही
        return []


# Example
nums = [2, 7, 11, 15]
target = 9

solution = Solution()

result = solution.twoSum(nums, target)

print(result)