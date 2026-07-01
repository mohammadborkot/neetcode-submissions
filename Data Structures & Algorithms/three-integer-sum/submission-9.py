class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(0, len(nums)):
            if nums[i] > 0: # if positive nothing else works
                break

            if i > 0 and nums[i] == nums[i - 1]: # skip dupes
                continue

            j = i+1
            k = len(nums)-1
            
            while j < k:
                # Too big, shrink right
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1

                # Too small, shrink left
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1

                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k: # skip dupes
                        j += 1
              
        return output
        