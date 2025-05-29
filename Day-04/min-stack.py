class MinStack:
    # stack with minimum tuple 
    # TC: O(1) SC: O(n)
    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        
    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)
        self.stack.append([val, self.minimum]) # make data structure such that each element has [value, minimum value at the time]

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minimum = self.stack[-1][1]
        else:
            self.minimum = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()