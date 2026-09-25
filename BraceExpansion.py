class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == ',':
                    # Union
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    # Parse inside braces
                    next_set, i = parse(i + 1)

                    # Concatenation
                    current = {
                        a + b
                        for a in current
                        for b in next_set
                    }

                else:
                    # Single lowercase letter
                    current = {
                        a + expression[i]
                        for a in current
                    }
                    i += 1

            # Add the last expression
            result |= current

            return result, i + 1 if i < len(expression) and expression[i] == '}' else i

        result, _ = parse(0)

        return sorted(result)
