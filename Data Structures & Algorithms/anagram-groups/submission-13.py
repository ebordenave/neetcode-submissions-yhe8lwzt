class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      prevMap = {}

      for word in strs:
        sorted_word = ''.join(sorted(word))

        if sorted_word not in prevMap:
          prevMap[sorted_word] = [word]

        else:
          prevMap[sorted_word].append(word)


      return [item for item in prevMap.values()]
        