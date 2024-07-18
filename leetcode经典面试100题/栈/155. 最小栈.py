class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.getMin() is not None:
            self.minStack.append(min(self.getMin(), val))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
obj.pop()
param_4 = obj.getMin()
print(param_4)
