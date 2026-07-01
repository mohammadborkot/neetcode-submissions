class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        # search for max k
        k = 0
        for n in piles:
            k = max(k, n)

        high = k
        low = 1

        while low <= high:
            k = int(low + (high - low) / 2)
            hours = 0
            # Compute hours with this k
            for pile in piles:
                hours += int(math.ceil(pile / k))

            # This K is too big
            if hours <= h:
                res = min(res, k)
                high = k - 1

            # This K is too small
            else:
                low = k + 1
            
        return res

