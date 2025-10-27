import math

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def euclidean(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_neighbors(maze, node, visited):
    rows, cols = len(maze), len(maze[0])
    x, y = node
    result = []
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if maze[nx][ny] != 1 and (nx, ny) not in visited:
                result.append((nx, ny))
    return result

def simplified_astar(maze, start, end):
    visited = set([start])
    path = [start]
    stack = []
    current = start
    while current != end:
        neighbors = get_neighbors(maze, current, visited)
        if not neighbors:
            # Dead end: backtrack to last multi-path point
            while stack:
                prev_cell, choices = stack.pop()
                # Remove the branch we already tried
                while choices and choices[0] in visited:
                    choices.pop(0)
                if choices:
                    current = choices.pop(0)
                    path = path[:path.index(prev_cell) + 1] + [current]
                    visited.add(current)
                    # If more choices remain, push back for future backtracking
                    if choices:
                        stack.append((prev_cell, choices))
                    break
            else:
                # No path found
                return [], visited
        elif len(neighbors) == 1:
            current = neighbors[0]
            path.append(current)
            visited.add(current)
        else:
            # Multiple choices: pick closest to end, save others for backtracking
            sorted_neighbors = sorted(neighbors, key=lambda cell: euclidean(cell, end))
            current = sorted_neighbors[0]
            path.append(current)
            visited.add(current)
            # Save multi-path point for backtracking
            if len(sorted_neighbors) > 1:
                stack.append((path[-2], sorted_neighbors[1:]))
    return path, visited

def print_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]
    for x, y in path:
        if maze_copy[x][y] == 0:
            maze_copy[x][y] = "*"
    for row in maze_copy:
        print(" ".join(str(c) for c in row))

def main():
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    path, visited = simplified_astar(maze, start, end)
    if path:
        print("Path found:")
        print(path)
        print("Cost (steps):", len(path) - 1)
        print("\nMaze with path marked as *:")
        print_maze_with_path(maze, path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
