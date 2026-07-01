class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            # Too big, move right
            if numbers[l] + numbers[r] > target:
                r -= 1
            # too little, move left
            if numbers[l] + numbers[r] < target:
                l += 1
        return [0, 0]
