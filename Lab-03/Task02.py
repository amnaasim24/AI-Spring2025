import random
import heapq
import time
from threading import Thread

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class DynamicAStar:
    def __init__(self, maze, start, goal, refresh_interval=2):
        self.maze = maze
        self.start = start
        self.goal = goal
        self.refresh_interval = refresh_interval
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.open_list = []
        self.closed_list = set()
        self.node_map = {}

    def run(self):
        start_node = Node(self.start)
        start_node.g = 0
        start_node.h = heuristic(self.start, self.goal)
        start_node.f = start_node.g + start_node.h
        heapq.heappush(self.open_list, start_node)
        self.node_map[self.start] = start_node
        
        while self.open_list:
            current_node = heapq.heappop(self.open_list)
            
            if current_node.position == self.goal:
                return self.reconstruct_path(current_node)
            
            self.closed_list.add(current_node.position)
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)
                
                if self.is_valid(neighbor_pos) and neighbor_pos not in self.closed_list:
                    g_cost = current_node.g + self.get_dynamic_cost(current_node.position, neighbor_pos)
                    if neighbor_pos not in self.node_map:
                        neighbor_node = Node(neighbor_pos, current_node)
                        self.node_map[neighbor_pos] = neighbor_node
                    else:
                        neighbor_node = self.node_map[neighbor_pos]
                    
                    if g_cost < neighbor_node.g:
                        neighbor_node.g = g_cost
                        neighbor_node.h = heuristic(neighbor_pos, self.goal)
                        neighbor_node.f = neighbor_node.g + neighbor_node.h
                        heapq.heappush(self.open_list, neighbor_node)

        return None

    def get_dynamic_cost(self, current_pos, neighbor_pos):
        if random.random() < 0.1:
            return random.randint(1, 10)
        else:
            return 1

    def is_valid(self, pos):
        x, y = pos
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] == 0

    def reconstruct_path(self, node):
        path = []
        while node:
            path.append(node.position)
            node = node.parent
        return path[::-1]

    def start_dynamic_updates(self):
        def dynamic_update():
            while True:
                time.sleep(self.refresh_interval)
                self.update_maze_dynamic_costs()
                print("Updated edge costs dynamically.")

        update_thread = Thread(target=dynamic_update)
        update_thread.daemon = True
        update_thread.start()

    def update_maze_dynamic_costs(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 0 and random.random() < 0.1:
                    self.maze[i][j] = 1
                elif self.maze[i][j] == 1 and random.random() < 0.1:
                    self.maze[i][j] = 0
        print("Maze updated!")

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

a_star = DynamicAStar(maze, start, goal)
a_star.start_dynamic_updates()
path = a_star.run()

if path:
    print("Path found:", path)
else:
    print("No path found")
