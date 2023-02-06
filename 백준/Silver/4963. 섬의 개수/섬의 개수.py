import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(x, y):
    if x<0 or y<0 or x>=h or y>=w :
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x-1, y-1)
        dfs(x, y-1)
        dfs(x+1, y-1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        dfs(x, y+1)
        dfs(x-1, y+1)
        return True
    
    return False

while 1:
    w, h = map(int, input().split())

    if w == h == 0:
        break
    
    cnt = 0
    graph = []

    for _ in range (h):
        graph.append(list(map(int, input().split())))

    for i in range (h):
        for j in range (w):
            if dfs(i, j) == True:
                cnt += 1
    
    print(cnt)