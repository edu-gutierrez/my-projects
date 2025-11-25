import random
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
        