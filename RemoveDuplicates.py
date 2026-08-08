#write code to remove duplicates form the array and find the distinct number of elements present in the array
#using two pointer approach
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


sol = Solution()

nums = [1, 1, 2, 2, 3, 3, 4]

result = sol.removeDuplicates(nums)

print(result)
##time complexity=o(n)
##space complexity=o(1)
