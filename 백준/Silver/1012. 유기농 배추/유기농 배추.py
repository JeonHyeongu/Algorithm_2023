import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    if check[x][y] == False and arr[x][y] == 1:
        check[x][y] = True
        for i in range(4):
            dfs(x + dx[i], y + dy[i])

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
    check = [[False for _ in range(m+1)] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    count = 0

    for i in range(n):
        for j in range(m):
            if check[i][j] == False and arr[i][j] == 1:
                for k in range(4):
                    dfs(i + dx[k], j + dy[k])
                count += 1
    print(count)