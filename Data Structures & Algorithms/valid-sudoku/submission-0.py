class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap_1 = defaultdict(set)
        hashmap_2 = defaultdict(set)
        hashmap_3 = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in hashmap_1[i] 
                    or board[i][j] in hashmap_2[j] 
                    or board[i][j] in hashmap_3[(i // 3, j // 3)]):
                    return False
                hashmap_1[i].add(board[i][j])
                hashmap_2[j].add(board[i][j])
                hashmap_3[(i // 3, j // 3)].add(board[i][j])
        return True

