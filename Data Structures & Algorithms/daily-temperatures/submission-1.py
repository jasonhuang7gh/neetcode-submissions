class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Use a stack
        # Whenever curr temp is higher than the one on top of stack, we've discovered
        # the next warmer day. Pop the stack and compute the difference in days.
        # Try again for the new highest in stack. If not warmer, stack curr temp.
        # Time: O(n) / Space: O(n)

        stack = []  # takes in [index, temp]
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:   # temperature on top of stack
                top_i, top_temp = stack.pop()
                result[top_i] = i - top_i
            stack.append([i, temp])

        return result


        # # Naive Solution
        # # Brute force - For each temperature, find next warmer temperature
        # # Time: O(n^2) / Space: O(n)

        # n = len(temperatures)
        # result = []

        # for i in range(n):
        #     j = 1
        #     warmer = False
        #     while i + j < n and not warmer:
        #         if temperatures[i + j] > temperatures[i]:
        #             result.append(j)
        #             warmer = True
        #         j += 1

        #     if not warmer:
        #         result.append(0)
        
        # return result