from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        def is_valid(string):
            balance = 0
            
            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    
                    if balance < 0:
                        return False
            
            return balance == 0

        queue = deque([s])
        visited = {s}
        
        while queue:
            size = len(queue)
            found = []
            
            for _ in range(size):
                current = queue.popleft()
                
                # If valid, this is minimum removal level
                if is_valid(current):
                    found.append(current)
                
                # Generate next level only if no valid string
                if not found:
                    for i in range(len(current)):
                        
                        # Only remove parentheses
                        if current[i] not in "()":
                            continue
                        
                        new_string = current[:i] + current[i + 1:]
                        
                        if new_string not in visited:
                            visited.add(new_string)
                            queue.append(new_string)
            
            # Once valid strings are found, don't go deeper
            if found:
                return found
        
        return [""]
