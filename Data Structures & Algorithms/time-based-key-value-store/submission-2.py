class TimeMap:

    def __init__(self):
        self.keys = {} # key : arr[ (value, timestamp)]
        self.times = set()
    
    # Insert a key to this TimeMap
    def set(self, key: str, value: str, timestamp: int) -> None:
        # First time insertion
        if key not in self.keys:
            self.keys[key] = [(value, timestamp)] 
        
        # Key present, but diff time stamp
        else:
            self.keys[key].append((value, timestamp))
        
        
    # Retrieve a key from this TimeMap
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""

        # arr[i] contains (value, timestamp)
        arr = self.keys[key]
        if timestamp < arr[0][1]:
            return ""

        # perform a bin search to find the timestamp
        l = 0
        r = len(arr)-1
        res = ["", -1]
        while l <= r:
            mid = l + (r - l) // 2

            # search top half
            if timestamp > arr[mid][1]:
                # upd default ans
                res[1] = max(res[1], arr[mid][1])
                res[0] = arr[mid][0]
                l = mid + 1

            # search bottom half
            elif timestamp < arr[mid][1]: 
                r = mid - 1
            
            # found
            else:
                return arr[mid][0]

        return res[0]


