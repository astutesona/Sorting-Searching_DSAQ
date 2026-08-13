def leftRotate(nums):
  first = nums[0]
  for i in range(1, len(nums)):
    nums[i-1] = nums[i]
  nums[-1] = first
nums=[7,6,5,4]
leftRotate(nums)
print(nums)

#output [6, 5, 4, 7]
## time ccomplexity o(n)
## space complexity=o(1)
