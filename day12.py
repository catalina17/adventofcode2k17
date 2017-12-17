import re


def DFS(node):
    global visited
    global graph

    visited[node] = True

    for child in graph[node]:
        if not child in visited:
            DFS(child)

if __name__ == '__main__':
    f = open("day12.txt", "r")
    graph = {}

    for line in f.readlines():
        nodes = re.split('\W+', line)
        graph[nodes[0]] = nodes[1:-1]

    visited = {}
    groups_count = 0
    for node in graph:
        if not node in visited:
            groups_count += 1
            DFS(node)
        print(len(visited.keys()))

    print(groups_count)
