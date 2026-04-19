from collections import deque
import heapq
import math

# ---------------- BFS ----------------
def bfs(grid):
    n = len(grid)
    start = (0, 0)

    # find treasure
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'T':
                target = (i, j)

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        x, y = queue.popleft()

        if (x, y) == target:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 'X' and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny))
                parent[(nx,ny)] = (x,y)

    return reconstruct_path(parent, start, target)


# ---------------- A* ----------------
def heuristic(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def astar(grid):
    n = len(grid)
    start = (0,0)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'T':
                target = (i,j)

    directions = [
        (1,0,1), (-1,0,1), (0,1,1), (0,-1,1),
        (1,1,1.4), (1,-1,1.4), (-1,1,1.4), (-1,-1,1.4)
    ]

    pq = [(0, start)]
    g_cost = {start: 0}
    parent = {}

    while pq:
        f, (x,y) = heapq.heappop(pq)

        if (x,y) == target:
            break

        for dx, dy, w in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 'X':
                new_g = g_cost[(x,y)] + w

                if (nx,ny) not in g_cost or new_g < g_cost[(nx,ny)]:
                    g_cost[(nx,ny)] = new_g
                    f_cost = new_g + heuristic((nx,ny), target)
                    heapq.heappush(pq, (f_cost, (nx,ny)))
                    parent[(nx,ny)] = (x,y)

    return reconstruct_path(parent, start, target)


# ---------------- Path reconstruction ----------------
def reconstruct_path(parent, start, target):
    path = []
    curr = target
    while curr in parent:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    path.reverse()
    return path


# ---------------- Example run ----------------
if __name__ == "__main__":
    grid = [
        ['S','0','0','0'],
        ['0','X','0','0'],
        ['0','0','0','T'],
        ['0','X','0','0']
    ]

    print("BFS Path:", bfs(grid))
    print("A* Path:", astar(grid))
