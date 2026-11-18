
class Solution2:
    def isValidSudoku(self, board) -> bool:
        hash = {'linha': {}, 'coluna': {}, 'matrix': {}}
        for i in range(9):
            for j in range(9):
                celula = board[i][j]
                if celula == '.':
                    continue
                celula = int(celula)

                if i not in hash['linha']:
                    hash['linha'][i] = set()

                if j not in hash['coluna']:
                    hash['coluna'][j] = set()

                operador = str(int(i/3)) + str(int(j/3))

                if operador not in hash['matrix']:
                    hash['matrix'][operador] = set()

                if celula in hash['linha'][i]:
                    print('linha')
                    print(i,j)
                    return False
                
                hash['linha'][i].add(celula)

                if celula in hash['coluna'][j]:
                    print('coluna')
                    print(i,j)
                    return False
                
                hash['coluna'][j].add(celula)

                if celula in hash['matrix'][operador]:
                    print('matrix')
                    print(i,j)
                    return False
                
                hash['matrix'][operador].add(celula)

        return True


s2 = Solution2()

board=[["1","2",".",".","3",".",".",".","."]
       ,["4",".",".","5",".",".",".",".","."]
       ,[".","9","8",".",".",".",".",".","3"]
       ,["5",".",".",".","6",".",".",".","4"]
       ,[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]

print(s2.isValidSudoku(board))