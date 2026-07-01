class Solution:
    def isValid(self, s: str) -> bool:

        COMPLIMENTS = {
            '(':')',
            '{':'}',
            '[':']'
        }
        open_braces = []

        # Add the opening & closing brackets to stacks
        for let in s:
            if let in COMPLIMENTS: # opening brace
                open_braces.append(let)

            else: #closing brace
                if len(open_braces) == 0:
                    return False

                open_let = open_braces.pop()
                if let != COMPLIMENTS[open_let]:
                    return False

        return len(open_braces) == 0
