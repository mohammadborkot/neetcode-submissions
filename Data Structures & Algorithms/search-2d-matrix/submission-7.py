class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0]) - 1

        while low <= high:
            mid = int(low + (high - low) / 2)
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            # Too high, check lower half
            if matrix[row][col] > target:
                high = mid - 1
            # Too low, check upper half
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                return True

        return False