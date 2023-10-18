
r, c = map(int, input().split())
l = [list(input()) for i in range(r)]
result = 1
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(r):
    for j in range(c):
        if l[i][j] == 'W':
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if l[nx][ny] == 'S':
                    result = 0
print(result)
if result == 1:
    for a in range(r):
        for b in range(c):
            if l[a][b] == '.':
                print('D', end='')
            else:
                print(l[a][b], end='')
        print()