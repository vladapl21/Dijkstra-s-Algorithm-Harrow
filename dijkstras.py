import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'Knoll': {'Bradbys': 8, 'Druries': 5, 'Moretons': 6},
    'Bradbys': {'Knoll': 8, 'Druries': 4, 'West Acre': 4},
    'Druries': {'Knoll': 5, 'Bradbys': 4, 'Moretons': 2, 'Newlands': 4, 'West Acre': 7},
    'Moretons': {'Druries': 2, 'Knoll': 6, 'Newlands': 6},
    'Newlands' : {'Druries': 4, 'Moretons': 6, 'West Acre': 11},
    'West Acre' : {'Newlands': 11, 'Druries': 7, 'Bradbys': 4}
}
start_vertex = 'Knoll'
distances = dijkstra(graph, start_vertex)
print(f'Shortest distances to Knoll from each house: {distances[]}')