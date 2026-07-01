class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = int(low + (high - low) / 2)

            # Too high, check lower half
            if nums[mid] > target:
                high = mid - 1
            # Too low, check upper half
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1