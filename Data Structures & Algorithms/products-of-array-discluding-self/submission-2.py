class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix and Suffix
        # Time: O(n) / Space: O(n)
        # WIP


        # Division - get total product and then divide by self (account for 0s)
        # Time: O(n) / Space: O(1)

        total_prod = 1
        one_zero = False   # if there are two or more 0's, answer is just list of 0's
        for num in nums:
            if num == 0:
                if not one_zero:
                    one_zero = True
                else:
                    total_prod = 0
                    return [0] * len(nums)
            else:
                total_prod *= num

        ans = [0 for i in range(len(nums))]
        # if there is only one 0, answer is list of 0's except for index where num is 0
        if one_zero:
            ans[nums.index(0)] = total_prod
        else:
            for i in range(len(nums)):
                ans[i] = total_prod // nums[i]
        
        return ans


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