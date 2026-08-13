class Solution:
  def rotate(self, nums, k):
    n= len(nums)

    k= k%n
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:1])
    nums.reverse()
nums = [1,2,3,4,5]
k=2
Solution().rotate(nums, k)
print(nums)

##output:[1, 2]
##time complexity of this problem: o(n)
## space complexity of this problem:o(1)
