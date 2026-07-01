class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # This map will contain anagram frequencies
        anagrams = {}
        for word in strs:
            counts = [0] * 26
            # compute frequencies
            for let in word:
                counts[ord(let) - ord('a')] += 1

            # add word to list of anagrams
            if tuple(counts) in anagrams:
                anagrams[tuple(counts)].append(word)
            else:
                anagrams[tuple(counts)] = [word]
        res = []
        for key in anagrams:
            res.append(anagrams[key])
        return res

