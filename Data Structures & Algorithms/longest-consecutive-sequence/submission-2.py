class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Use a set for O(1) lookup of consecutive numbers
        # For each number n in set, look at the number lower and after
        # If lower is not in set, then the sequence starts with n
        # If higher is in set, then increase the streak length
        # Time: O(n)

        nums_set = set(nums)
        streak = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                curr = 1
                while (num + curr) in nums_set:
                    curr += 1
                streak = max(streak, curr)
        
        return streak


        # # Naive solution: Sort first
        # # Time: O(n*log(n))

        # if len(nums) == 0:
        #     return 0
        
        # nums.sort()
        # last, curr, streak = nums[0], 1, 1

        # for num in nums:
        #     if num - last > 1:
        #         streak = max(curr, streak)
        #         curr = 1
        #         last = num
        #     else:
        #         if num != last:
        #             last += 1
        #             curr += 1
        
        # return max(curr, streak)