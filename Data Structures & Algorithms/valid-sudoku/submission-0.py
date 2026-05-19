class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_rows = [set() for _ in range(9)]
        check_cols = [set() for _ in range(9)]
        check_grids = [set() for _ in range(9)]
        
        def getGridIndex(rowId, colId):
            return int((rowId//3)*3+(colId//3))
        
        for rowId, row in enumerate(board):
            for colId, val in enumerate(row):
                if val == ".":
                    continue
                else:
                    if val in check_rows[rowId] or val in check_cols[colId] or val in check_grids[getGridIndex(rowId, colId)]:
                        return False
                    else:
                        check_rows[rowId].add(val)
                        check_cols[colId].add(val)
                        check_grids[getGridIndex(rowId, colId)].add(val)
        return True