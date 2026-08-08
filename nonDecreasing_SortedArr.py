class Solution:
    def isSorted(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False

        return True


sol = Solution()

nums = [1, 2, 2, 4, 5]

print(sol.isSorted(nums))
