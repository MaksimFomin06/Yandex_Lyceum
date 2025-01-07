import csv
from heapq import heappush, heappop


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, u = heappop(priority_queue)
        
        if current_distance > distances[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heappush(priority_queue, (distance, v))
    
    return distances[end]


def find_cheapest_path(input_file):
    graph = {}
    with open(input_file, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if len(row) >= 3 and row[2]:  # Пропускаем строки с пустой ценой
                source, destination, cost = row[:3]
                cost = int(cost)
                if source not in graph:
                    graph[source] = []
                graph[source].append((destination, cost))
    
        route = next(reader)
        start_city, end_city = route[0], route[1]
    
    direct_cost = dijkstra(graph, start_city, end_city)
    
    one_transfer_cost = float('inf')
    for intermediate_city in set(graph.keys()) - {start_city, end_city}:
        try:
            first_leg_cost = dijkstra(graph, start_city, intermediate_city)
            second_leg_cost = dijkstra(graph, intermediate_city, end_city)
            total_cost = first_leg_cost + second_leg_cost
            if total_cost < one_transfer_cost:
                one_transfer_cost = total_cost
        except KeyError:
            pass
    
    cheapest_cost = min(direct_cost, one_transfer_cost)
    return cheapest_cost


input_file = 'input.csv'
cheapest_path = find_cheapest_path(input_file)
print(cheapest_path)