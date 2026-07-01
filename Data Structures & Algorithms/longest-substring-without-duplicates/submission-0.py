class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        seen = set()
        length = 0
        while j < len(s):
            # dupe character
            while s[j] in seen:
                # shrink left side
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            length = max(length, j - i + 1)
            j += 1

        return length