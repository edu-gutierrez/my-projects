import random
import heapq
from collections import deque

def generate_maze(grid, probability):

    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if (r == 0 and c == 0) or (r == rows-1 and c == cols-1):
                grid[r, c] = 3
            
            elif random.random() < probability:
                grid[r, c] = 1 

def bfs(grid, start, end):
    rows, cols = grid.shape
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    parent_map = {} 
    directions = [(1, 0), (0,-1), (0, 1), (-1, 0)]
    found = False

    while queue:
        current = queue.popleft()
        row, column = current

        if current == end:
            found = True
            break 

        for dr, dc in directions:
            newr, newc = row + dr, column + dc

            if 0 <= newr < rows and 0 <= newc < cols:
                if grid[newr, newc] != 1 and (newr, newc) not in visited:
                    queue.append((newr, newc))
                    visited.add((newr, newc))
                    parent_map[(newr, newc)] = current
                    
                    if (newr, newc) != end:
                         yield ("visit", newr, newc)

    if found:
        curr = end
        while curr in parent_map:
            yield ("path", curr[0], curr[1]) 
            curr = parent_map[curr]
        yield ("path", start[0], start[1]) 
    else:
        print("No hay camino")

def dfs(grid, start, end):
    rows, cols = grid.shape
    stack = [start]
    visited = set() 
    
    parent_map = {} 
    directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    found = False

    while stack:
        current = stack.pop()
        row, column = current

        if current in visited:
            continue
        
        visited.add(current)
        
        if current != start and current != end:
             yield ("visit", row, column)

        if current == end:
            found = True
            break 

        for dr, dc in directions:
            newr, newc = row + dr, column + dc

            if 0 <= newr < rows and 0 <= newc < cols:
                if grid[newr, newc] != 1 and (newr, newc) not in visited:
                    stack.append((newr, newc))
                    
                    if (newr, newc) not in parent_map:
                        parent_map[(newr, newc)] = current

    if found:
        curr = end
        while curr != start:
            yield ("path", curr[0], curr[1]) 
            curr = parent_map[curr]
        yield ("path", start[0], start[1]) 
    else:
        print("No hay camino")
        
def a_star(grid, start, end):
    rows, cols = grid.shape
    
    count = 0 # Para desempatar
    open_set = []
    heapq.heappush(open_set, (0, count, start))
    
    open_set_hash = {start} #Para que acceder a un elemento sea O(1) y no O(n)
    closed_set = set()

    parent_map = {}
    g_score = {} 
    f_score = {}

    for r in range(rows):
        for c in range(cols):
            node = (r, c)
            g_score[node] = float("inf")
            f_score[node] = float("inf")

    g_score[start] = 0
    f_score[start] = _heuristic(start, end)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    found = False

    while open_set:
        current = heapq.heappop(open_set)[2]
        open_set_hash.remove(current)
        
        if current in closed_set:
            continue
        closed_set.add(current)

        row, col = current

        if current != start and current != end:
            yield("close", row, col)

        if current == end:
            found = True
            break

        for dr, dc in directions:
            newr, newc = row + dr, col + dc

            if newr < rows and newr >= 0 and newc < cols and newc >= 0:
                if grid[newr, newc] == 1 or (newr, newc) in closed_set:
                    continue

                tmp_g_score = g_score[current] + 1

                if tmp_g_score < g_score[(newr, newc)]:
                    parent_map[(newr, newc)] = current
                    g_score[(newr, newc)] = tmp_g_score
                    f_score[(newr, newc)] = tmp_g_score + _heuristic((newr, newc), end)
                    
                    if (newr, newc) not in open_set_hash:
                        count += 1
                        heapq.heappush(open_set, (f_score[(newr, newc)], count, (newr, newc)))
                        open_set_hash.add((newr, newc))
                        
                        if (newr, newc) != end:
                            yield ("visit", newr, newc)

    if found:
        curr = end
        while curr in parent_map:
            yield ("path", curr[0], curr[1])
            curr = parent_map[curr]
        yield ("path", start[0], start[1])
    else:
        print("No hay camino")

def _heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)