class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix[0]) - 1
        arr = 0
        while matrix[arr][R] < target:
            if arr == len(matrix) - 1:
                break
            arr += 1

        
        while L <= R:
            M = L + ((R-L) // 2)
            print(M)
            if matrix[arr][M] == target:
                return True
            elif matrix[arr][M] > target:
                R = M - 1
            else:
                L = M + 1
        return False
        