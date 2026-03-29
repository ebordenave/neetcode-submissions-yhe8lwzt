class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = {} # hashmap to store my results
      
      for word in strs:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word not in res:
          res[sorted_word] = [word]
          
        else:
          res[sorted_word].append(word)

      return [item for item in res.values()]