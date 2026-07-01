class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        s_freqs = {}
        t_freqs = {}
        
        meets_reqs = False
        # we can check length of or window
        # if == len(t) and every char in s is in t then its fine
        # or at minimum it must be len(t)

        # count frequences of letters in t
        for let in t:
            t_freqs[let] = t_freqs.get(let, 0) + 1

        need = len(t_freqs)
        have = 0
        j = 0 # left window
        res = [-1, -1]
        size = float('inf')

        for i in range(0, len(s)): 
            let = s[i]
            s_freqs[let] = s_freqs.get(let, 0) + 1
            if let in t_freqs and s_freqs[let] == t_freqs[let]:
                have += 1

            # shrink left while our requirements are met
            while have == need:
                # upd min substring
                if (i - j) < size:
                    res[1] = i
                    res[0] = j
                    size = i - j

                # shrink left
                s_freqs[s[j]] -= 1
                if s[j] in t_freqs and s_freqs[s[j]] < t_freqs[s[j]]:
                    have -= 1
                j += 1

        return s[res[0]:res[1]+1]
                




            
        

