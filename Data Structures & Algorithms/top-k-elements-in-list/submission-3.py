class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort - create a list of lists with indices as frequencies.
        # Append the num into the list of correct freq like adding into a bucket.
        # Then starting from largest freq bucket and descending, return k most freq.
        # Time: O(n) / Space: O(n)
        # Time is faster because no sort is necessary. But space is actually O(2n)
        # which is more than using a heap O(n + k).

        nums_freq = {}
        for num in nums:
            if num in nums_freq:
                nums_freq[num] += 1
            else:
                nums_freq[num] = 1

        # max number of freqs is length of nums list (+1 to account for 0 index)
        freq_buckets = [[] for i in range (len(nums) + 1)]
        for num, freq in nums_freq.items():
            freq_buckets[freq].append(num)

        ans = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        
        # # Using a heap makes sense when asking for the top k frequent.
        # # Push (freq, num) pairs into the heap and remove the smallest whenever
        # # the heap grows beyond size k because it won't be part of the answer.
        # # Time: O(n * log(k)) / Space: O(n + k)
        # # This is faster than sorting a hashmap of size n because the heap is  
        # # size k, but needs more space due to an addition of a heap.
        # nums_freq = {}
        # for num in nums:
        #     if num in nums_freq:
        #         nums_freq[num] += 1
        #     else:
        #         nums_freq[num] = 1
        # heap = []
        # for num in nums_freq.keys():
        #     heapq.heappush(heap, (nums_freq[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # ans = []
        # for i in range(k):
        #     freq, num = heapq.heappop(heap)
        #     ans.append(num)
        # return ans


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
