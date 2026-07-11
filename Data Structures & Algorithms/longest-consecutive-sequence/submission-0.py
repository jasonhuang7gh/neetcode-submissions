class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Naive solution: Sort first
        # Time: O(n*log(n))

        if len(nums) == 0:
            return 0
        
        nums.sort()
        last, curr, streak = nums[0], 1, 1

        for num in nums:
            if num == last:
                continue
            elif num - last == 1:
                last += 1
                curr += 1
            else:
                streak = max(curr, streak)
                curr = 1
                last = num
        
        return max(curr, streak)