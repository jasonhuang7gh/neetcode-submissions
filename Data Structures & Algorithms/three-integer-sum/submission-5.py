class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Select one number and then search for the other two using two pointers.
        # Sort first to skip duplicates. Left pointer starts after first number, 
        # right pointer starts at the end. If current sum is too large, move right
        # pointer left to reduce it, and vice-versa. When sum is 0, store triplet.
        # Time: O(n^2) / Space: O(1)
        
        nums.sort()
        ans = []

        for i in range(len(nums)):
            num = nums[i]
            if num > 0:   # remaining numbers are positive
                break
            if i and num == nums[i - 1]:  # skip duplicates
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                # store triplet, and move both pointers inward
                else:   
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return ans


        # # Use a hash map to store freq of each num.
        # # When first and second numbers are selected, check if third is in map.
        # # Decrement count from hash map when selecting the first two numbers,
        # # and increment back to normal in next iteration.
        # # Sort nums first to identify duplicates to skip them.
        # # Time: O(n^2) / Space: O(n)
        # nums.sort()
        # freqs = {}
        # for num in nums:
        #     if num in freqs:
        #         freqs[num] += 1
        #     else:
        #         freqs[num] = 1
        # ans = []
        # for i in range(len(nums)):
        #     freqs[nums[i]] -= 1
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     for j in range(i + 1, len(nums)):
        #         freqs[nums[j]] -= 1
        #         if j > i + 1 and nums[j] == nums[j - 1]:
        #             continue
        #         # nums[i] + nums[j] + target = 0
        #         target = -(nums[i] + nums[j])
        #         if target in freqs and freqs[target] > 0:
        #             ans.append([nums[i], nums[j], target])
        #     for j in range(i + 1, len(nums)):
        #         freqs[nums[j]] += 1
        # return ans


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