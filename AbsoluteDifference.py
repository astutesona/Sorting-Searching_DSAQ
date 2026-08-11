class Solution:
    def findCount(self, arr, num, diff):
        count = 0

        for element in arr:
            if abs(element - num) <= diff:
                count += 1

        if count == 0:
            return -1

        return count


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))

    arr = list(map(int, input("Enter array elements: ").split()))

    num = int(input("Enter num: "))
    diff = int(input("Enter diff: "))

    solution = Solution()

    result = solution.findCount(arr, num, diff)

    print("Output:", result)

# Time Complexity: O(n)
# Space Complexity: O(1) excluding the input array.

  
