n, a = int(input()), {i: 1 for i in map(int, input().split())}
m, b = int(input()), list(map(int, input().split()))

for i in range(len(b)):
    print(a.get(b[i], 0))
