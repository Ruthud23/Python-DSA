class Solution:
    def countIslands(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    stack = [(i, j)]
                    total = grid[i][j]
                    grid[i][j] = 0

                    while stack:
                        r, c = stack.pop()

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr = r + dr
                            nc = c + dc

                            if (0 <= nr < rows and
                                0 <= nc < cols and
                                grid[nr][nc] > 0):

                                total += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))

                    if total % k == 0:
                        count += 1

        return count