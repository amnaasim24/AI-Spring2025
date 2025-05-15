import heapq



class GoalBasedAgentDFS:
    def __init__(self, start_node, goal, graph):
        self.current_node = start_node
        self.goal = goal
        self.graph = graph
        self.visited = set()
        
    def actions(self, node):
        return self.graph.get(node, [])
    
    def goal_test(self):
        return self.current_node == self.goal
    
    def plan(self):
        stack = [self.current_node]
        
        while stack:
            node = stack.pop()
            if node not in self.visited:
                self.visited.add(node)
                
                if self.goal_test():
                    return f"Goal {self.goal} found at node {node}!"
                
                for neighbor in self.actions(node):
                    if neighbor not in self.visited:
                        stack.append(neighbor)
                        
        return "Goal not found!"
    
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

agent = GoalBasedAgentDFS('A', 'F', graph)
print(agent.plan())






class GoalBasedAgentDLS:
    def __init__(self, start_node, goal, graph, max_depth):
        self.current_node = start_node
        self.goal = goal
        self.graph = graph
        self.max_depth = max_depth
        self.visited = set()
        
    def actions(self, node):
        return self.graph.get(node, [])
    
    def goal_test(self):
        return self.current_node == self.goal
    
    def plan(self, depth=0):
        if depth > self.max_depth:
            return "Depth limit reached"
        
        if self.goal_test():
            return f"Goal {self.goal} found at node {self.current_node}!"
        
        self.visited.add(self.current_node)
        
        for neighbor in self.actions(self.current_node):
            if neighbor not in self.visited:
                result = GoalBasedAgentDLS(neighbor, self.goal, self.graph, self.max_depth).plan(depth + 1)
                if "Goal" in result:
                    return result
        return "Goal not found within depth limit"
    
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

agent = GoalBasedAgentDLS('A', 'F', graph, 2)
print(agent.plan())






class UtilityBasedAgentUCS:
    def __init__(self, start_node, goal, graph, costs):
        self.start_node = start_node
        self.goal = goal
        self.graph = graph
        self.costs = costs
        self.visited = set()

    def actions(self, node):
        return self.graph.get(node, [])
    
    def goal_test(self, node):
        return node == self.goal
    
    def plan(self):
        queue = [(0, self.start_node)]
        heapq.heapify(queue)
        
        while queue:
            current_cost, current_node = heapq.heappop(queue)
            
            if current_node in self.visited:
                continue
                
            self.visited.add(current_node)
            
            if self.goal_test(current_node):
                return f"Goal {self.goal} found with total cost {current_cost}"
            
            for neighbor in self.actions(current_node):
                if neighbor not in self.visited:
                    new_cost = current_cost + self.costs.get((current_node, neighbor), float('inf'))
                    heapq.heappush(queue, (new_cost, neighbor))
        
        return "Goal not found"
    
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

costs = {
    ('A', 'B'): 1,
    ('A', 'C'): 4,
    ('B', 'D'): 2,
    ('B', 'E'): 5,
    ('C', 'F'): 3,
    ('E', 'F'): 1
}

agent = UtilityBasedAgentUCS('A', 'F', graph, costs)
print(agent.plan())
