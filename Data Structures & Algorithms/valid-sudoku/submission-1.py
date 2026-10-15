class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = collections.defaultdict(set)

        for r in range(9):
                seen = set()

                for c in range(9):
                    n = board[r][c]

                    if n == ".":
                        continue

                    if n in seen:
                        return False
                    else:
                        seen.add(n)

                    if(board[r][c] in squares[(r //3, c // 3)]):
                        return False
                    squares[(r // 3, c// 3)].add(board[r][c])

        for c in range(9):
                seen = set()

                for r in range(9):
                    n = board[r][c]

                    if n == ".":
                        continue
                    
                    if n in seen:
                        return False

                    seen.add(n)

        return True