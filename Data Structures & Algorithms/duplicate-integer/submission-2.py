class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # track duplicate entries
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        
        # No duplicates
        return False
        