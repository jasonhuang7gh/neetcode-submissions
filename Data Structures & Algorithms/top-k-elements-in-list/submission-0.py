class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Brute force - Store frequency of each integer in hashmap and then sort
        # Time: O(n * log(n)) / Space: O(n)

        nums_freq = {}
        for num in nums:
            if num in nums_freq:
                nums_freq[num] += 1
            else:
                nums_freq[num] = 1
        
        sorted_freqs = sorted(nums_freq.values())
        ans = []

        for num, freq in nums_freq.items():
            if freq in sorted_freqs[(-1 * k):]:
                ans.append(num)
        
        return ans
