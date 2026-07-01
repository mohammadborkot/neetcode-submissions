class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1

        # Find the row target is on 
        for r in range(0, len(matrix)):
            if matrix[r][0] > target:
                break
            elif matrix[r][0] == target:
                return True
            row += 1
            
        if row == -1:
            return False
        
        # perform bin search on the row
        low = 0
        high = len(matrix[row])-1
        while low <= high:
            mid = int(low + (high - low) / 2)
            # Too high, check lower half
            if matrix[row][mid] > target:
                high = mid - 1
            # Too low, check upper half
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                return True

        return False