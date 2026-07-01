class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i in range(0, len(nums)):
            pairs[nums[i]] = i

        for i in range(0, len(nums)):
            j = target - nums[i]
            if j in pairs and pairs[j] != i:
                return [i, pairs[j]]