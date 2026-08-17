class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Prefix and Suffix
        # From left to right, get product of nums left of nums[i] for prefixes
        # From right to left, get product of nums right of nums[i] for suffixes
        # Multiply prefix[i] and suffix[i] for product without nums[i]
        # Time: O(n) / Space: O(n) 

        n = len(nums)
        prefix_list = [0] * n
        suffix_list = [0] * n
        # Set first element of prefix_list to 1 because there is no prod left of nums[0]
        # Do the same for last element of suffix_list because no prod right of nums[n-1]
        prefix_list[0] = suffix_list[n - 1] = 1

        for i in range(1, n):
            prefix_list[i] = nums[i - 1] * prefix_list[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix_list[i] = nums[i + 1] * suffix_list[i + 1]

        ans = []
        for i in range(n):
            ans.append(prefix_list[i] * suffix_list[i])
        return ans


        # # Division - get total product and then divide by self (account for 0s)
        # # Time: O(n) / Space: O(1) extra space
        # total_prod = 1
        # one_zero = False   # if there are two or more 0's, answer is just list of 0's
        # for num in nums:
        #     if num == 0:
        #         if not one_zero:
        #             one_zero = True
        #         else:
        #             total_prod = 0
        #             return [0] * len(nums)
        #     else:
        #         total_prod *= num
        # ans = [0 for i in range(len(nums))]
        # # if there is only one 0, answer is list of 0's except for index where num is 0
        # if one_zero:
        #     ans[nums.index(0)] = total_prod
        # else:
        #     for i in range(len(nums)):
        #         ans[i] = total_prod // nums[i]
        # return ans


        # # Brute force - Time limit exceeded
        # # Nested for loop to multiply each number except for self
        # # Time: O(n^2) / Space: O(1)
        # ans = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             prod *= nums[j]
        #     ans.append(prod)
        # return ans