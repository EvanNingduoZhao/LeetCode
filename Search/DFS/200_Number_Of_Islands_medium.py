#这道题基本和695一样，只不过这道题是数有多少个单独的岛
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        counter = 0
        stack = []
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                if grid[r][c] == "1":
                    stack.append((r, c))
                    counter += 1
                while stack:
                    row, col = stack.pop()
                    for direction in directions:
                        newRow = row + direction[0]
                        newCol = col + direction[1]
                        if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
                            continue
                        if grid[newRow][newCol] == "1":
                            stack.append((newRow, newCol))
                            grid[newRow][newCol] = 0
        return counter
