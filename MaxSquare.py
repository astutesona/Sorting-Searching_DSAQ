class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        result = []

        while sum > 0 and len(result) < num:
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit

        result.extend(['0'] * (num - len(result)))

        return ''.join(result)
