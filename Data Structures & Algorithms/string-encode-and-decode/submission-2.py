class Solution:

    def encode(self, strs: List[str]) -> str:
        # %length%word%lengthword%
        # or 
        # length%wordlengthword
        # so we could jump length times across word
        # we would know to record length by %

        encoded = []
        for word in strs:
            encoded.append(str(len(word)) + "%" + word)
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            # get the length 
            j = i
            while s[j] != "%":
                j += 1
            length = int(s[i:j])
            output.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return output


                
        