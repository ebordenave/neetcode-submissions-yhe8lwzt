class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights)-1
        max_area = 0

        while l < r:

            width = r - l
            length = min(heights[l], heights[r])
            current_area = length * width

            if heights[l] > heights[r]:
                r -= 1

            else:
                l += 1

            max_area = max(current_area, max_area)
        return max_area


        