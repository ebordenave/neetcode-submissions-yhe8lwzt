class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:

            # if it current char is not a letter, increment by 1
            if s[l].isalnum() == False:
                l += 1
                continue
            # if it current char is not a letter, decrement by 1
            if s[r].isalnum() == False:
                r -= 1
                continue

            if (s[l].lower() != s[r].lower()):
                return False

            l += 1
            r -= 1

        return True