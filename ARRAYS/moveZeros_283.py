#broute force lavna paddel aand pahle non zero elements woith order eka temp veriable madhe store kartil
class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        temp =[]
        for i in range(0,n):
            if nums[i] != 0:
                temp.append(nums[i])
        
        nz=len(temp)
        for i in range(0,nz):
            nums[i] = temp[i]
        for i in range(nz,n):
            nums[i]=0
            
nums = [0,1,0,3,12]
solution=Solution()
result = solution.moveZeroes(nums)
print(nums)
            