class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Start with two pointers: one at the beginning (left) and one at the end (right)
        l, r = 0, len(s) - 1

        # Keep checking characters while left is before right
        while l < r:
            # Move the left pointer forward if the current character is not a letter or number
            while l < r and not self.is_alpha(s[l]):
                l += 1

            # Move the right pointer backward if the current character is not a letter or number
            while l < r and not self.is_alpha(s[r]):
                r -= 1

            # Compare the characters at left and right (case-insensitive)
            # If they don't match, it's not a palindrome
            if s[l].lower() != s[r].lower():
                return False

            # Move both pointers toward the center
            l += 1
            r -= 1

        # If we checked all matching characters and didn't return False, it's a palindrome
        return True

    # Helper function to check if a character is a letter or number
    def is_alpha(self, c: str):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
