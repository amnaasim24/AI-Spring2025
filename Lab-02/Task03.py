from collections import deque

class IterativeDeepeningDFS:
    def __init__(self, start_node, goal, graph, max_depth):
        self.start_node = start_node
        self.goal = goal
        self.graph = graph
        self.max_depth = max_depth

    def actions(self, node):
        return self.graph.get(node, [])
    
    def goal_test(self, node):
        return node == self.goal
    
    def dfs(self, node, depth):
        if depth == 0:
            if self.goal_test(node):
                return [node]
            return None
        elif depth > 0:
            for neighbor in self.actions(node):
                path = self.dfs(neighbor, depth - 1)
                if path:
                    return [node] + path
        return None

    def plan(self):
        for depth in range(self.max_depth + 1):
            result = self.dfs(self.start_node, depth)
            if result:
                return result
        return "Goal not found"

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

agent = IterativeDeepeningDFS('A', 'F', graph, max_depth=3)
print("IDDFS Path:", agent.plan())





class BidirectionalSearch:
    def __init__(self, start_node, goal, graph):
        self.start_node = start_node
        self.goal = goal
        self.graph = graph

    def bfs(self, start, goal, visited):
        queue = deque([(start, [start])])
        visited.add(start)
        
        while queue:
            node, path = queue.popleft()
            
            if node == goal:
                return path
            
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def plan(self):
        visited_start = set()
        visited_goal = set()
        
        queue_start = deque([(self.start_node, [self.start_node])])
        queue_goal = deque([(self.goal, [self.goal])])
        
        visited_start.add(self.start_node)
        visited_goal.add(self.goal)
        
        while queue_start and queue_goal:
            path_start = self.bfs(self.start_node, self.goal, visited_start)
            if path_start:
                return path_start
            
            path_goal = self.bfs(self.goal, self.start_node, visited_goal)
            if path_goal:
                return path_goal[::-1]

        return "Goal not found"

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

agent = BidirectionalSearch('A', 'F', graph)
print("Bidirectional Search Path:", agent.plan())
