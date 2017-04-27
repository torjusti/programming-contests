import sys

targets = [[2, 2],[1, 2]]
prices = [1, 1, 10]
defaultPrice = 1

position = [0, 0]

moves = [
    [
        [0, 1],
        [1, 0],
        [-1, 0],
    ], [
        [1, 0],
        [0, -1],
        [0, 1],
    ], [
        [0, -1],
        [-1, 0],
        [1, 0],
    ], [
        [-1, 0],
        [0, 1],
        [0, -1],
    ]
]

distances = [{}, {}, {}, {}]

def distance(start, end, heading):
    queue = [[start, 0, heading, []]]

    shortestPath = False
    shortestPathHeading = 0

    while queue:
        vertex = queue.pop(0)

        key = str(vertex[0][0]) + str(vertex[0][1])

        heading = vertex[2]

        if key in distances[heading]:
            if str(end[0]) + str(end[1]) in distances[heading][key]:
                return distances[heading][key][str(end[0]) + str(end[1])]

        if shortestPath and vertex[1] > shortestPath:
            continue

        if vertex[0] == end:
            if not shortestPath:
                shortestPath = vertex[1]
                shortestPathHeading = heading
            else:
                shortestPath = min(vertex[1], shortestPath)
                shortestPathHeading = heading
            continue

        for i, move in enumerate(moves[heading]):
            if vertex[3] == [i, i]:
                continue

            queue.extend([[[vertex[0][0] + move[0], vertex[0][1] + move[1]], vertex[1] + prices[i] + defaultPrice, (vertex[2] + i) % 2, vertex[3] + [i]]])

    return [shortestPath, shortestPathHeading]


for heading in range(4):
    for a in range(5):
        for b in range(5):
            distances[heading][str(a) + str(b)] = {}

            for c in range(5):
                for d in range(5):
                    if a == c and b == d or c == 0 and d == 0:
                        continue
                    distances[heading][str(a) + str(b)][str(c) + str(d)] = distance([a, b], [c, d], heading)

sum = 0
heading = 0
prev = [0, 0]

for target in targets:
    dist = distances[heading][str(prev[0]) + str(prev[1])][str(target[0]) + str(target[1])]
    sum += dist[0]
    heading = dist[1]
    prev = target

print sum
