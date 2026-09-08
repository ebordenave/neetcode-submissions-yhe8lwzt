class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxRun = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                currentCount = 1

                while num + 1 in numsSet:
                    num += 1
                    currentCount += 1

                maxRun = max(maxRun, currentCount)
        return maxRun