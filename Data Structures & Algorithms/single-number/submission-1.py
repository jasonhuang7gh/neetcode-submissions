class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Using XOR (numbers that appear twice cancel each other out)
        # Time: O(n) / Space: O(1)
        # ans = 0
        # for num in nums:
        #     ans ^= num
        # return ans

        # Using a set to track an encountered number
        # Time: O(n) / Space: O(n)
        num_set = set()
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
        return num_set.pop()


