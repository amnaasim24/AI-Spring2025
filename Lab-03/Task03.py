import math
import heapq

class DeliveryPoint:
    def __init__(self, id, x, y, start_time, end_time):
        self.id = id
        self.x = x
        self.y = y
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"DeliveryPoint({self.id}, {self.x}, {self.y}, [{self.start_time}, {self.end_time}])"

def heuristic(current, next_point, current_time):
    distance = math.sqrt((current.x - next_point.x) ** 2 + (current.y - next_point.y) ** 2)
    urgency = max(0, next_point.end_time - current_time)
    return distance + urgency

def greedy_best_first_search(delivery_points, start_point):
    route = [start_point]
    current_time = 0
    remaining_points = set(delivery_points)
    remaining_points.remove(start_point)
    
    while remaining_points:
        best_point = None
        best_heuristic = float('inf')
        
        for point in remaining_points:
            h = heuristic(route[-1], point, current_time)
            if h < best_heuristic:
                best_point = point
                best_heuristic = h
        
        if current_time <= best_point.end_time:
            route.append(best_point)
            remaining_points.remove(best_point)
            current_time += 1
        else:
            continue
    
    return route

delivery_points = [
    DeliveryPoint(1, 2, 3, 2, 5),
    DeliveryPoint(2, 4, 6, 1, 4),
    DeliveryPoint(3, 5, 7, 3, 6),
    DeliveryPoint(4, 1, 1, 0, 3)
]

start_point = DeliveryPoint(0, 0, 0, 0, 0)

route = greedy_best_first_search(delivery_points, start_point)

print("Optimized delivery route:", route)

for point in route:
    print(f"Deliver to point {point.id} at ({point.x}, {point.y}) within time window {point.start_time}-{point.end_time}")
