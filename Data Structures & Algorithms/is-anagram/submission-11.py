class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # early exit, if lengths are unequal, return False
      if len(s) != len(t):
        return False
      
      # count initialization and check 
      # then compare
      
      count_s = {}
      
      for c in s:
        count_s[c] = 1 + count_s.get(c, 0)
      
      count_t = {}
      
      for c in t:
        count_t[c] = 1 + count_t.get(c, 0)
        
        
      return count_t == count_s
        