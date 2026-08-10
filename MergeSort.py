class MergeSort:
    def sort(self, nums):
       
        if len(nums) <= 1:
            return nums

        temp = [0] * len(nums)

        self.merge_sort(nums, temp, 0, len(nums) - 1)

        return nums

    def merge_sort(self, nums, temp, left, right):
     
        if left >= right:
            return

        mid = left + (right - left) // 2

        self.merge_sort(nums, temp, left, mid)


        self.merge_sort(nums, temp, mid + 1, right)

        if nums[mid] <= nums[mid + 1]:
            return


        self.merge(nums, temp, left, mid, right)

    def merge(self, nums, temp, left, mid, right):
        i = left
        j = mid + 1
        k = left

     
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1

     
        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1

    
        for i in range(left, right + 1):
            nums[i] = temp[i]


nums = [38, 27, 43, 3, 9, 82, 10]

obj = MergeSort()
result = obj.sort(nums)

print("Sorted Array:", result)
# time complexity of this sort :
## Average Case:o(nlogn)
## Worst Case :o(nlogn)
##Best case: o(nlogn)
# Space =o(n)
# for the temporary array

