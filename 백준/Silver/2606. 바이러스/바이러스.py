import sys
input = sys.stdin.readline

computer = int(input())
network = int(input())
graph = [[] for i in range (computer + 1)]

visited = [0]*(computer + 1)

for i in range (network):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(start):
    stack = [start]
    visited[start] = 1

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if visited[adj] == 0:
                visited[adj] = 1
                stack.append(adj)

dfs(1)
print(sum(visited) - 1)