class Solution:
    def numIslands(self, grid) -> int:
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                if visited[i][j]:
                    continue

                if grid[i][j] == "1":
                    islands += 1

                    visited[i][j] = True

                    stack = []
                    stack.append([i,j])

                    while(stack):
                        x, y = stack.pop()

                        for coord in [ [0,1], [0,-1], [1, 0], [-1, 0] ]:
                            newX = x + coord[0]
                            newY = y + coord[1]

                            if newX < 0 or newX >= rows or newY < 0 or newY >= cols:
                                continue

                            if visited[newX][newY]: continue

                            if grid[newX][newY] == "1":
                                visited[newX][newY] = True

                                stack.append([newX, newY])
            print(visited[i])
                

        return islands

s = Solution()

print(s.numIslands([
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]))