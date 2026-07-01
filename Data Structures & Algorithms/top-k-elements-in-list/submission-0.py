class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Store frequencies of each number
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        # Form an array where i represents i occurrences
        top = [[] for _ in range(len(nums))]
        for n in counts:
            top[counts[n] - 1].append(n)

        # Compute top K most frequent elements
        res = []
        for i in range(len(top)-1, -1, -1):
            for n in top[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res



