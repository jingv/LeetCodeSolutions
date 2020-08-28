# def orangesRotting(self, grid: List[List[int]]) -> int:
def orangesRotting(grid):
    time = 0
    result = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                result.append((i, j, time))
    while result:
        m, n, time = result.pop(0)
        for direction in directions:
            new_m, new_n = m + direction[0], n + direction[1]
            if new_m in range(len(grid)) and new_n in range(len(grid[0])) and grid[new_m][new_n] == 1:
                grid[new_m][new_n] = 2
                result.append((new_m, new_n, time + 1))
    for i in grid:
        if 1 in i:
            return -1
    return time
        

def orangesRotting2(grid):
    from collections import deque
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    m,n,time = len(grid),len(grid[0]),0
    result = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                result.append((i,j,time))
    while result:
        x,y,time = result.popleft()
        for direction in directions:
            x_new,y_new = x+direction[0],y+direction[1]
            if 0 <= x_new < m and 0 <= y_new < n and grid[x_new][y_new] == 1:
                grid[x_new][y_new] = 2
                result.append((x_new,y_new,time+1))
    for row in grid:
        if 1 in row:
            return -1
    return time


def main():
    grids = [[[2,1,1],[1,1,0],[0,1,1]], [[2,1,1],[0,1,1],[1,0,1]], [[0,2]]]
    for grid in grids:
        print(orangesRotting(grid), "   ", orangesRotting2(grid))    


if __name__ == "__main__":
    main()