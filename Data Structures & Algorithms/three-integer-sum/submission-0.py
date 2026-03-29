class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # Sort the array to enable two-pointer technique and handle duplicates
        nums.sort()
        
        # Iterate through array, treating each number as the first element of a potential triplet
        for idx, val in enumerate(nums):
            # Optimization: if the smallest remaining number is positive,
            # no three numbers can sum to zero (all remaining are positive)
            if val > 0:
                break
            
            # Skip duplicate values for the first element to avoid duplicate triplets
            # Example: [-1, -1, 0, 1] - only process the first -1, skip the second
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            # Use two-pointer approach to find pairs that sum to -val
            # This is the classic "Two Sum II" pattern on the remaining sorted array
            l, r = idx + 1, len(nums) - 1
            
            while l < r:
                three_sum = val + nums[l] + nums[r]
                
                # If sum is too large, move right pointer left to decrease sum
                if three_sum > 0:
                    r -= 1
                # If sum is too small, move left pointer right to increase sum
                elif three_sum < 0:
                    l += 1
                # Found a valid triplet that sums to zero
                else:
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Skip duplicate values for the second element
                    # Example: after finding [-1, 0, 1], if next left is also 0, skip it
                    # Check l < r first to avoid index out of bounds
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return result