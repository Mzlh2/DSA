class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        copymatrix = []
        for r in range(rows):
            rowArr=[] 
            for c in range(cols):
                rowArr.append(matrix[r][c])
            copymatrix.append(rowArr)

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for j in range(cols):
                        copymatrix[r][j] = 0
                    for i in range(rows):
                        copymatrix[i][c] = 0
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = copymatrix[r][c]   