class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0
        while l < r:
            # compute current volume
            curr_vol = (r - l) * min(heights[l], heights[r])
            max_water = max(curr_vol, max_water)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_water