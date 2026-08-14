class Solution:

    def moveZeroes(self, nums):

        j = 0

        # Step 1: Move all non-zero elements to the front
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Step 2: Fill the remaining positions with zero
        while j < len(nums):
            nums[j] = 0
            j += 1


# Create object
obj = Solution()

# Input array
nums = [0, 1, 0, 3, 12]

# Call the method
obj.moveZeroes(nums)

# Print the result
print(nums)
