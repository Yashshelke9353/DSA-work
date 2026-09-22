# Input:
# ["a"]

# Output:
# ["a"]

# Return:
# 

# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# Output:
# ["a","b","1","2"]
# 12

class Solution:
    def compress(self, chars):

        write = 0
        read = 0

        while read < len(chars):

            current = chars[read]
            count = 0

            while read < len(chars) and chars[read] == current:
                read += 1
                count += 1

            chars[write] = current
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write