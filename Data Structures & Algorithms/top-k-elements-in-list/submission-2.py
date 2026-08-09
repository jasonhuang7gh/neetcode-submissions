class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        # WIP
        
        # Using a heap makes sense when asking for the top k frequent.
        # Push (freq, num) pairs into the heap and remove the smallest whenever
        # the heap grows beyond size k because it won't be part of the answer.
        # This is faster than sorting a hashmap of size n because the heap is  
        # size k, but needs more space due to an addition of a heap.
        # Time: O(n * log(k)) / Space: O(n + k)
        nums_freq = {}
        for num in nums:
            if num in nums_freq:
                nums_freq[num] += 1
            else:
                nums_freq[num] = 1
        
        heap = []
        for num in nums_freq.keys():
            heapq.heappush(heap, (nums_freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            ans.append(num)
        return ans


        # # Brute force - Store frequency of each integer in hashmap and then sort
        # # Time: O(n * log(n)) / Space: O(n)
        # nums_freq = {}
        # for num in nums:
        #     if num in nums_freq:
        #         nums_freq[num] += 1
        #     else:
        #         nums_freq[num] = 1
        # sorted_freqs = sorted(nums_freq.values())
        # ans = []
        # for num, freq in nums_freq.items():
        #     if freq in sorted_freqs[(-1 * k):]:
        #         ans.append(num)
        # return ans
