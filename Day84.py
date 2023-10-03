def isSafe(graph, color, n, c):
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] and color[j] == c:
                return False
    return True

def graphColoring(graph, m, i, color, n):
    if i == n:
        if isSafe(graph, color, n, m):
            display(color)
            return True
        return False

    for j in range(1, m + 1):
        color[i] = j
        if graphColoring(graph, m, i + 1, color, n):
            return True
        color[i] = 0
    return False

def display(color):
    print("1")

n = int(input())
m = int(input())
e = int(input())
graph = []

for i in range(n):
    a = []
    for j in range(n):
        a.append(0)
    graph.append(a)

for i in range(e):
    a = int(input())
    b = int(input())
    graph[a][b] = 1
    graph[b][a] = 1

color = [0 for i in range(n)]
if not graphColoring(graph, m, 0, color, n):
    print("0")
