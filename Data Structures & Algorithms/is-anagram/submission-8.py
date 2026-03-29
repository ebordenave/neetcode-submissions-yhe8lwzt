class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # check length of s and t
      # if the lengths are not equal
      # return False
      if len(s) != len(t):
        return False
      
      # create a defaultdict of s that will track
      # the counts of each char in s
      count_s = defaultdict(int)
      
      # populate the dict with a counting each instance of
      # char in s
      for char in s:
        count_s[char] += 1
        
      for char in t:
        if char not in count_s:
          return False
      
      # if a char is in s and is NOT in t
      # return False
      # else for each char in t that is in s, subtract 1
        else:
          count_s[char] -= 1
      
      # once we've looped through the entire string
      # we check if the value of any of the keys are greater than or less than zero
      # if they are, that means there is an unequal count and therefore is not an anagram
      for key, value in count_s.items():
        if value > 0 or value < 0:
          return False
      
      # else return True
      return True