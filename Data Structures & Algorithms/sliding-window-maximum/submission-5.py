import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        pq = [] 
        l = 0
        for r in range(0, len(nums)):
            # Add this number to our heap
            heapq.heappush(pq, (-nums[r], r))
            
            # Reached maximum window length, append to res 
            if (r - l + 1) == k: 
                # Clean the heap
                while pq[0][1] < l:
                    heapq.heappop(pq)
                # Add max num
                max_num = pq[0][0] * -1
                res.append(max_num)
                l += 1
        return res

