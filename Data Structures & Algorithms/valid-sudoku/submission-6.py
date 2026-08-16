class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      rows = collections.defaultdict(set)
      cols = collections.defaultdict(set)
      squares = collections.defaultdict(set)

      for r in range(9):
        for c in range(9):

          board_value = board[r][c]

          if board_value == '.':
            continue

          squares_sub_region = (r//3, c//3)

          if (board_value in rows[r] or
              board_value in cols[c] or
              board_value in squares[squares_sub_region]):
             
            return False


          rows[r].add(board_value)
          cols[c].add(board_value)
          squares[squares_sub_region].add(board_value)

      return True
        