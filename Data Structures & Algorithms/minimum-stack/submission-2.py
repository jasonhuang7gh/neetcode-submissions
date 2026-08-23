class MinStack:

    # Keep a stack just for finding minimum so getMin is O(1) time

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            curr_min = self.min_stack[-1]
            self.min_stack.append(min(curr_min, val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


    # # Brute force
    # def __init__(self):
    #     self.stack = []
    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    # def pop(self) -> None:
    #     self.stack.pop()
    # def top(self) -> int:
    #     return self.stack[-1]
    # def getMin(self) -> int:
    #     return min(self.stack)
