class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # from this list, group together
        # words that are anagrams of e/o

        anagrams = {} # map frequencies -> [] of words

        for i in range(0, len(strs)):
            word = strs[i]

            # count frequencies of word
            counts = [0]*26
            for j in range(0, len(word)):
                counts[ord(word[j]) - ord('a')] += 1
            if tuple(counts) in anagrams:
                anagrams[tuple(counts)].append(word)
            else:
                anagrams[tuple(counts)] = [word]

        res = []
        for key in anagrams:
            res.append(anagrams[key])
            
        return res