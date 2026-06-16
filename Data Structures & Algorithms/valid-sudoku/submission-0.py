class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                boxid = (r//3,c//3)
                value = board[r][c]
                if value == ".":
                    continue
                if value in row[r] or value in column[c] or value in box[boxid]:
                    return False
                row[r].add(value)
                column[c].add(value)
                box[boxid].add(value)
        return True                


        