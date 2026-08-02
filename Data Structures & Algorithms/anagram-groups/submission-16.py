class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            # print(sorted_word)
            if sorted_word not in groups:
                groups[sorted_word] = [word]

            else:
                groups[sorted_word].append(word)

        return [item for item in groups.values()]


        