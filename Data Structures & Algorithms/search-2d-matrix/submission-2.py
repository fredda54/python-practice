class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot = len(matrix) - 1
        top = 0
        while top <= bot:
            row = top + ((bot - top) // 2)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        L = 0
        R = len(matrix[0]) - 1
        while L <= R:
            M = L + ((R-L) // 2)
            if matrix[row][M] == target:
                return True
            elif matrix[row][M] > target:
                R = M - 1
            else:
                L = M + 1
        return False
        