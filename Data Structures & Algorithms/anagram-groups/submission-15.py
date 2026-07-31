class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in group:
                group[sorted_word] = [word]

            else:
                group[sorted_word].append(word)

        return [i for i in group.values()]
        