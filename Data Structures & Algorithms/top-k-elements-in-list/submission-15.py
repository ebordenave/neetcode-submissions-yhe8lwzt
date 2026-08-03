class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      # create a hashmap for count
      count = {}


      # the trick to use the the freq[value] for each index
      # [ 1, 2, 2, 3, 3, 3 ]
      # [ 0 | 1 | 2 | 3 | 4 | 5 ]
      #       1   2   3

      # initialize a empty bucket
      freq = [[] for i in range(len(nums) + 1)]

      #{ value : num_of_occurences }

      for num in nums:
        count[num] = 1 + count.get(num, 0)
        
      print(count)

      for num, count in count.items():
        freq[count].append(num)

      # check for understanding here
      # print(freq)
      #[[],[1],[2],[3], [], [], []]

      # initialize a result list
      res = []

      # and then iterate through the freq arrary backwards
      for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
          res.append(n)

          if len(res) == k:
            return res

      # append to result

      # if length of result equals k

      # return result
