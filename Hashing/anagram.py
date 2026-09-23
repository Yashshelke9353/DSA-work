class Solution:

    def isAnagram(self, s, t):

        # Length different असेल तर anagram होऊ शकत नाही
        if len(s) != len(t):
            return False

        # Character ची frequency store करण्यासाठी dictionary
        count = {}

        # s मधील प्रत्येक character check करा
        for char in s:

            # Character आधी dictionary मध्ये नसेल
            if char not in count:
                count[char] = 1

            # Character आधीपासून असेल तर count वाढवा
            else:
                count[char] += 1

        # t मधील प्रत्येक character check करा
        for char in t:

            # t मधील character s मध्येच नसेल
            if char not in count:
                return False

            # Character ची frequency कमी करा
            count[char] -= 1

            # Count 0 पेक्षा कमी झाला तर
            # t मध्ये तो character जास्त वेळा आहे
            if count[char] < 0:
                return False

        # सर्व characters match झाले
        return True


# Example
s = "anagram"
t = "nagaram"

solution = Solution()

result = solution.isAnagram(s, t)

print(result)