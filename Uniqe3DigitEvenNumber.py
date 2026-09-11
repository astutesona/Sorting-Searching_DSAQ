class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        # Count frequency of each digit
        for digit in digits:
            freq[digit] += 1

        count = 0

        # Check all 3-digit numbers
        for num in range(100, 1000):

            # Number must be even
            if num % 2 != 0:
                continue

            # Extract digits
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Count digits required for this number
            needed = [0] * 10
            needed[a] += 1
            needed[b] += 1
            needed[c] += 1

            # Check if we have enough copies of every digit
            possible = True

            for digit in range(10):
                if needed[digit] > freq[digit]:
                    possible = False
                    break

            if possible:
                count += 1

        return count
