class Solution:
    def isPalindrome(self, n):
        original = n
        reverse = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10

        return original == reverse


obj = Solution()

n = 121
result = obj.isPalindrome(n)

print(result)

## Finding palindrome using two pointer method
s = input("Enter a string: ")

left = 0
right = len(s) - 1

is_palindrome = True

while left < right:

    if s[left] != s[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

## class based Solution
class Solution:

    def isPalindrome(self, s):

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


obj = Solution()

s = "madam"

result = obj.isPalindrome(s)

print(result)

    
