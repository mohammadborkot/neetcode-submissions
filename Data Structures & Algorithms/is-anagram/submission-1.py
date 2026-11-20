class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # For this, we can count frequencies
        
        # char frequencies of s
        s_freq = [0]*26
        for let in s:
            s_freq[ord(let) - ord('a')] += 1

        t_freq = [0]*26
        for let in t:
            t_freq[ord(let) - ord('a')] += 1
        
        return s_freq == t_freq