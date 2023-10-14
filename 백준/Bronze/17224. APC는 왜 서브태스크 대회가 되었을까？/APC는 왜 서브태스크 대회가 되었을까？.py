n, l, k = map(int, input().split())
level = [[i for i in list(map(int, input().split()))] for j in range(n)]
# print(level)

score = 0
arr = sorted(level, key=lambda x: x[1])
count, i = 0, 0

while count < k and i < len(level):
    if arr[i][1] <= l:
        score += 140
        count += 1
    elif arr[i][1] > l and arr[i][0] <= l:
        score += 100
        count += 1
    i += 1

print(score)