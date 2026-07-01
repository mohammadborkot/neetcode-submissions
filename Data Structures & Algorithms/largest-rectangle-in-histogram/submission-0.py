class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair: (index, height)

        for i in range(0, len(heights)):
            start = i
            bar = heights[i]

            # Extend if this elem is greater than top of stack
            while stack and stack[-1][1] > bar:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, bar))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area