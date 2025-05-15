from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current_pos, end_pos):
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

def best_first_search(maze, start, goals):
    rows, cols = len(maze), len(maze[0])
    current_position = start
    total_path = []

    while goals:
        nearest_goal = min(goals, key=lambda goal: heuristic(current_position, goal))
        
        path = best_first_search_single_goal(maze, current_position, nearest_goal)
        
        if path is None:
            print("No path found to the goal!")
            return None

        total_path.extend(path[:-1])
        current_position = nearest_goal
        goals.remove(nearest_goal)

    return total_path

def best_first_search_single_goal(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start)
    end_node = Node(end)
    frontier = PriorityQueue()
    frontier.put(start_node)
    visited = set()
    visited.add(start)

    while not frontier.empty():
        current_node = frontier.get()
        current_pos = current_node.position

        if current_pos == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
                new_node = Node(new_pos, current_node)
                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_pos, end)
                new_node.f = new_node.h
                frontier.put(new_node)
                visited.add(new_pos)

    return None

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goals = [(4, 4), (1, 4)]

path = best_first_search(maze, start, goals)
if path:
    print("Path found:", path)
else:
    print("No path found")
