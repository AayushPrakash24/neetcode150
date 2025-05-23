class Solution:
    def isValid(self, s: str) -> bool:
        # classic stack problem
        # TC: O(n) SC: O(n)
        stack = []
        matches = {"{":"}", "[":"]", "(":")"}

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                e = stack.pop()
                if c != matches[e]:
                    return False
        
        return not stack