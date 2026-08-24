class MinStack:

    # Use one stack, but store val and min_val as a pair
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            curr_min = min(val, self.stack[-1][1])
            self.stack.append([val, curr_min])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


    # # Keep a stack just for finding minimum so getMin is O(1) time
    # def __init__(self):
    #     self.stack = []
    #     self.min_stack = []
    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if self.min_stack:
    #         curr_min = self.min_stack[-1]
    #         self.min_stack.append(min(curr_min, val))
    #     else:
    #         self.min_stack.append(val)
    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.min_stack.pop()
    # def top(self) -> int:
    #     return self.stack[-1]
    # def getMin(self) -> int:
    #     return self.min_stack[-1]


    # # Brute force for getMin is O(n) time
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
