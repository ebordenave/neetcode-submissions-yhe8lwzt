class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      rows = defaultdict(set)
      cols = defaultdict(set)
      squares = defaultdict(set)

      for r in range(9):
        for c in range(9):


          boardValue = board[r][c]

          if boardValue == ".":
            continue

          sub_region = (r//3,c//3)

          if(boardValue in rows[r] or
            boardValue in cols[c] or
            boardValue in squares[sub_region]):
            return False

          rows[r].add(boardValue)
          cols[c].add(boardValue)
          squares[sub_region].add(boardValue)

      return True
        