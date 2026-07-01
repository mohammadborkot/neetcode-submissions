class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seqs = {}
        seen = set()
        count = 0
        for n in nums:
            seen.add(n)

        for n in nums:
            # start of sequence
            if n-1 not in seen and n-1 not in seqs:
                seqs[n] = n

        for key in seqs:
            num = seqs[key]
            curr = 0
            while num in seen:
                curr += 1
                num += 1
            count = max(count, curr)
        
        return count