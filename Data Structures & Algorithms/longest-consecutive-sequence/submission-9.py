class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_run = 0

        for i in range(len(nums)):
            current_run = 1

            if nums[i] - 1 not in nums_set:
                start = nums[i]

                while start + 1 in nums_set:
                    start += 1
                    current_run += 1

                max_run = max(max_run, current_run)

        return max_run

        