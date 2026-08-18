class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if (1 << i) & n:
                ans += 1
        return ans