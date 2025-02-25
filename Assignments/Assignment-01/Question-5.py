import heapq
from collections import deque

# Romania map graph with road distances
romania_map = {
    "Arad": [("Zerind", 75), ("Timisoara", 118), ("Sibiu", 140)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Urziceni", 85), ("Giurgiu", 90)],
    "Giurgiu": [("Bucharest", 90)],
    "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
    "Eforie": [("Hirsova", 86)],
    "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
    "Iasi": [("Vaslui", 92), ("Neamt", 87)],
    "Neamt": [("Iasi", 87)]
}

# Heuristic values (straight-line distance to Bucharest)
heuristic = {
    "Arad": 366, "Zerind": 374, "Oradea": 380, "Sibiu": 253, "Timisoara": 329,
    "Lugoj": 244, "Mehadia": 241, "Drobeta": 242, "Craiova": 160, "Rimnicu Vilcea": 193,
    "Fagaras": 176, "Pitesti": 100, "Bucharest": 0, "Giurgiu": 77, "Urziceni": 80,
    "Hirsova": 151, "Eforie": 161, "Vaslui": 199, "Iasi": 226, "Neamt": 234
}

# BFS Algorithm
def bfs(start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    while queue:
        node, path, cost = queue.popleft()
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, distance in romania_map.get(node, []):
                queue.append((neighbor, path + [neighbor], cost + distance))
    return None, float("inf")

# UCS Algorithm
def ucs(start, goal):
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, distance in romania_map.get(node, []):
                heapq.heappush(queue, (cost + distance, neighbor, path + [neighbor]))
    return None, float("inf")

# Greedy Best-First Search
def greedy_bfs(start, goal):
    queue = [(heuristic.get(start, float("inf")), start, [start], 0)]
    visited = set()
    while queue:
        _, node, path, cost = heapq.heappop(queue)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, distance in romania_map.get(node, []):
                heapq.heappush(queue, (heuristic.get(neighbor, float("inf")), neighbor, path + [neighbor], cost + distance))
    return None, float("inf")

# Iterative Deepening Depth-First Search
def dls(node, goal, depth, path, cost, visited):
    if depth < 0:
        return None, float("inf")
    if node == goal:
        return path, cost
    visited.add(node)
    for neighbor, distance in romania_map.get(node, []):
        if neighbor not in visited:
            result, result_cost = dls(neighbor, goal, depth - 1, path + [neighbor], cost + distance, visited.copy())
            if result:
                return result, result_cost
    return None, float("inf")

def iddfs(start, goal):
    depth = 0
    while True:
        visited = set()
        result, cost = dls(start, goal, depth, [start], 0, visited)
        if result:
            return result, cost
        depth += 1

# User Input
print("Cities available:", ", ".join(romania_map.keys()))
start_city = input("Enter the source city: ").strip()
goal_city = input("Enter the destination city: ").strip()

# Validate input
if start_city not in romania_map or goal_city not in romania_map:
    print("Invalid city name! Please enter a valid city from the list.")
else:
    bfs_path, bfs_cost = bfs(start_city, goal_city)
    ucs_path, ucs_cost = ucs(start_city, goal_city)
    gbfs_path, gbfs_cost = greedy_bfs(start_city, goal_city)
    iddfs_path, iddfs_cost = iddfs(start_city, goal_city)


    print("\nResults:")
    print("BFS Path:", bfs_path, "| Cost:", bfs_cost)
    print("UCS Path:", ucs_path, "| Cost:", ucs_cost)
    print("Greedy BFS Path:", gbfs_path, "| Cost:", gbfs_cost)
    print("IDDFS Path:", iddfs_path, "| Cost:", iddfs_cost)

    # Sorting the algorithms by cost
    results = [
        ("BFS", bfs_path, bfs_cost),
        ("UCS", ucs_path, ucs_cost),
        ("Greedy BFS", gbfs_path, gbfs_cost),
        ("IDDFS", iddfs_path, iddfs_cost)
    ]

    results.sort(key=lambda x: x[2])

    print("\nAlgorithm Rankings (Least to Most Costly):")
    for algo, path, cost in results:
        print(f"{algo}: Path: {path} | Cost: {cost}")
