class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res

            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            # if r > mid then ignore right side
            if nums[mid] >= nums[l]:
                l = mid + 1
            
            else: # min is in right side
                r = mid - 1

        return res
