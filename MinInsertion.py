
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open_needed += 1
                i += 1
            else:
                # A closing pair requires two ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    insertions += 1
                    i += 1

                if open_needed > 0:
                    open_needed -= 1
                else:
                    insertions += 1

        return insertions + 2 * open_needed
