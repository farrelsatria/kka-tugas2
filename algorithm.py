import heapq
import math

def eucledian(coord, start, dest):
    x1, y1 = coord[start]
    x2, y2 = coord[dest]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def greedy_bfs(graph, coord, start, dest):
    visited = set()

    h_start = eucledian(coord, start, dest)
    frontier = [(h_start, start, [start], 0)]

    while frontier:
        h_now, curr_city, path, cost_total = heapq.heappop(frontier)

        if curr_city == dest:
            return path, cost_total

        if curr_city in visited:
            continue

        visited.add(curr_city)

        for neighbour, cost in graph[curr_city].items():
            if neighbour not in visited:
                cost_new = cost_total + cost
                h_neighbour = eucledian(coord, neighbour, dest)
                path_new = path + [neighbour]
                heapq.heappush(frontier, (h_neighbour, neighbour, path_new, cost_new))

    return None, None

def a_star(graph, coord, start, dest):
    visited = set()

    h_start = eucledian(coord, start, dest)
    frontier = [(h_start, start, [start], 0)]

    while frontier:
        f_now, curr_city, path, cost_total = heapq.heappop(frontier)

        if curr_city == dest:
            return path, cost_total

        if curr_city in visited:
            continue

        visited.add(curr_city)

        for neighbour, cost in graph[curr_city].items():
            if neighbour not in visited:
                g_new = cost_total + cost
                h_neighbour = eucledian(coord, neighbour, dest)
                f_new = g_new + h_neighbour
                path_new = path + [neighbour]
                heapq.heappush(frontier, (f_new, neighbour, path_new, g_new))

    return None, None