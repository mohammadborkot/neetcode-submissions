class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Thoughts
        # Compare counts of s1 to s2
        # if let in s1 exists in s2 of <= freq, is permutation
        s1_freq = [0]*26
        s2_freq = [0]*26

        # count char freqs of s1
        for let in s1:
            s1_freq[ord('a') - ord(let)] += 1

        l = 0
        r = 0

        while r < len(s2):
    
            # Count frequencies of s2
            s2_freq[ord('a') - ord(s2[r])] += 1

            # freq of current letter
            s2_count = s2_freq[ord('a') - ord(s2[r])]
            s1_count = s1_freq[ord('a') - ord(s2[r])]
            
            while s2_count > s1_count or s1_count == 0 and l <= r:
                s2_freq[ord('a') - ord(s2[l])] -= 1
                s2_count = s2_freq[ord('a') - ord(s2[r])]
                s1_count = s1_freq[ord('a') - ord(s2[r])] 
                l += 1
            # Check if freqs are equal
            if s1_freq == s2_freq:
                return True
            r += 1

        return False