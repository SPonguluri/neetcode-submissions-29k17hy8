class MinStack:

    def __init__(self):
        self.stack = []      # stores all pushed values
        self.minStack = []   # stores the minimum value up to each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Compute new minimum: min of current val and previous minimum
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]