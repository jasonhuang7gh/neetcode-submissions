class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # Brute force - multiply x by itself n times with for loop
        # Time: O(n) / Space: O(1)
        power = 1
        for i in range(abs(n)):
            power *= x
        if n >= 0:
            return power
        else:
            return 1 / power

