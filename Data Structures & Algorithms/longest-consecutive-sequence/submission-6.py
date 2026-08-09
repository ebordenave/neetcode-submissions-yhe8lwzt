class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxRun = 0

        numsSet = set(nums)

        for num in numsSet:
            if num - 1 not in numsSet:
                currentMax = 1
                currentNum = num

                while currentNum + 1 in numsSet:
                    currentNum += 1
                    currentMax += 1
            
                maxRun = max(maxRun, currentMax)

        return maxRun
