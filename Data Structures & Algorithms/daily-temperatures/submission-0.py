class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Naive Solution
        # Brute force - For each temperature, find next warmer temperature
        # Time: O(n^2)

        n = len(temperatures)
        result = []

        for i in range(n):
            j = 1
            warmer = False
            while i + j < n and not warmer:
                if temperatures[i + j] > temperatures[i]:
                    result.append(j)
                    warmer = True
                j += 1

            if not warmer:
                result.append(0)
        
        return result