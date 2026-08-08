class Solution:
    def isSorted(self,nums):
        for i in range (len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        return True
sol=Solution()
#nums=[1,2,3,4,5,6]
nums=[1,2,6,4,5]
print(sol.isSorted(nums))

time complexity of this code will be =o(n)
space complexity of this code will be=o(1)
because here i am using only one datastructure
