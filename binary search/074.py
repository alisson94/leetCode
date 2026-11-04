class Solution:
    def searchMatrix(self, matrix, target):
        inicio = 0
        m = len(matrix)
        n = len(matrix[0])
        fim = m*n

        while inicio < fim:
            meio = int((inicio + fim)/2)
            y = meio%n - 1
            x = int((meio-y+ 1)/n)

            print(meio)
            print(x)
            print(y)

            

            if matrix[x][y] == target:
                return True
            
            if target > matrix[x][y]:
                inicio = meio+1
                continue
            if target < matrix[x][y]:
                fim = meio
                continue
        
        return False
            

        
s = Solution()

print(s.searchMatrix([[1]], 31))