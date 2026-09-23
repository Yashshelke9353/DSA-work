class Solution:

    def majorityElement(self, nums):

        # Dictionary मध्ये प्रत्येक number ची frequency store करू
        count = {}

        # Array मधील प्रत्येक number check करा
        for num in nums:

            # Number dictionary मध्ये नसेल तर count = 1
            if num not in count:
                count[num] = 1

            # Number आधीपासून असेल तर count वाढवा
            else:
                count[num] += 1

        # Majority element शोधण्यासाठी
        for num in count:

            # जर number n/2 पेक्षा जास्त वेळा आला असेल
            if count[num] > len(nums) // 2:

                # तो majority element आहे
                return num