class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0

        while l < r:
            width = (r - l)
            ht = min(heights[l],heights[r])
            current_area = width * ht

            max_area = max(current_area, max_area)

            if heights[l] <= heights[r]:
                l += 1

            else:
                r -= 1

        return max_area