n=int(input("Enter a number: "))
fact=1
for i in range(1, n+1):
  fact=fact*i
print("Factorial:", fact)

##time complexity=o(n)
##space complexity=o(1)

## class Based Solution to find factorial of any number
class Solution:
  def factorial(Self, n):
    fact=1
    for i in range(1, n+1):
      fact= fact*i
    return fact
obj=Solution()
n=5
result=obj.factorial(n)
print(result)
# Time Complexity: O(n)
# Space Complexity: O(1)
