class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0]*26
        t_count = [0]*26

        for let in s:
            s_count[ord(let) - ord('a')] += 1

        for let in t:
            t_count[ord(let) - ord('a')] += 1
        
        return s_count == t_count