class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(0, len(temperatures)):

            while len(stack) > 0:
                if temperatures[i] > temperatures[stack[-1]]:
                    # pop until the top is smaller
                    top = stack.pop() # this is an index
                    # solution of the popped item is this
                    res[top] = i - top
                else: 
                    break
            
            # Add to stack if less
            stack.append(i)
        return res