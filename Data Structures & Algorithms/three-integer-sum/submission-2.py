class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Two pointers
        # WIP


        # Use a hash map to store freq of each num.
        # When first and second numbers are selected, check if third is in map.
        # Decrement count from hash map when selecting the first two numbers,
        # and increment back to normal in next iteration.
        # Sort nums first to identify duplicates to skip them.
        # Time: O(n^2) / Space: O(n)
        nums.sort()
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        ans = []
        for i in range(len(nums)):
            freqs[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                freqs[nums[j]] -= 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # nums[i] + nums[j] + target = 0
                target = -(nums[i] + nums[j])
                if target in freqs and freqs[target] > 0:
                    ans.append([nums[i], nums[j], target])
            for j in range(i + 1, len(nums)):
                freqs[nums[j]] += 1
        return ans


        # # Brute force - sum every triplet 
        # # Time: O(n^3) / Space: O(1)
        # # use a set to prevent duplicate triplets
        # triplet_set = set()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 # use tuples instead of list because set can't store lists
        #                 triplet_set.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        # ans = []
        # # reconvert tuples into lists
        # for triplet in triplet_set:
        #     ans.append(list(triplet))
        # return ans