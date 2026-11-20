class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # could have array of size == k
        # ith repres
        counts = {} # map num -> count

        # pass 1, count frequencies
        for i in range(0, len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        # array of size nums + 1
        top = []
        for _ in range(0, len(nums) + 1):
            top.append([])
        
        for key in counts:
            top[counts[key]].append(key)
        
        res = []
        for i in range(len(top) - 1, -1, -1):
            for num in top[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return [0, 0]
        