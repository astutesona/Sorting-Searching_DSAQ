class Solution:
  def secondLargest(self, nums):
    largest=[0]
    secondLargest=-1
    for i in range(1, len(nums)):
      if nums[i]>largest:
        secondLargest=largest
        largest=nums[i]
        
      elif nums[i] >secondLargest and nums[i]!=largest:
        secondLargest=nums[i]
        return secondLargest

##time complexity: o(n)
## space complexity=o(1)
