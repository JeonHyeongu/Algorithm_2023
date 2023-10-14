
def teacher(c):
    for i in range(len(c)):
        if c[i] % 2 != 0:
            c[i] += 1
    return c

def check(d):
    if len(set(d)) == 1:
        return True
    else:
        return False

def water(e):
    f, g = [0]*len(e), [0]*len(e)
    for i in range(len(e)):
        f[i] = e[i]//2
    for j in range(len(e)):
        if j == 0:
            g[0] = f[0] + f[len(e)-1]
        else:
            g[j] = f[j] + f[j-1]
    return g

t= int(input())
for i in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    arr = teacher(c)
    count = 0
    while not check(arr):
        arr = water(arr)
        # print(arr)
        arr = teacher(arr)
        # print(arr)
        count += 1
    print(count)