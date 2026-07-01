class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)

        for i in range(0, len(temperatures)):
            start_temp = temperatures[i]
            for j in range(i+1, len(temperatures)):
                new_temp = temperatures[j]
                if new_temp > start_temp:
                    output[i] = j - i 
                    break
        return output
