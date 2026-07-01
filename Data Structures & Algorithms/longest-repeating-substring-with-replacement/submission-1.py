class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        freqs = {}
        most_freq = 0 # most occurrences of a letter
        max_length = 0
        while j < len(s):
            # upd freqs
            freqs[s[j]] = freqs.get(s[j], 0) + 1

            most_freq = max(most_freq, freqs[s[j]]) # record max 
            length = j - i + 1

            while length - most_freq > k: # No more replacements
                freqs[s[i]] -= 1
                most_freq = max(most_freq, freqs[s[i]])
                i += 1
                length = j - i + 1
            
            max_length = max(max_length, length)
            j += 1
           # "ABCAABABB"
        return max_length 

    





        