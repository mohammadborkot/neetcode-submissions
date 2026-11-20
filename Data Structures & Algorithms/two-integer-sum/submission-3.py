class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {} # maps num -> index

        for i in range(0, len(nums)):
            need[nums[i]] = i
        
        for i in range(0, len(nums)):
            diff = target - nums[i]

            if diff in need and need[diff] != i:
                return [i, need[diff]]
        
        return [0, 0]

