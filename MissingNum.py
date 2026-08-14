class Solution:
  def missingNumber(Self, nums):
    n= len(nums)
    xor =0
    for i in range(n+1):
      xor = xor ^ i

    for nums in nums:
      xor =xor ^ nums
    return xor
obj = Solution()
nums = [3,0,1]
print(obj.missingNumber(nums))
## output =2 
## time complexity =o(n)
## space complexity=o(1)
