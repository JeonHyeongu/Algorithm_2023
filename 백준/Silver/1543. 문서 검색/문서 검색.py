a = list(input())
t = list(input())
count = 0
ck = [False] * len(a)
for i in range(len(a)-len(t)+1):
    if t[:] == a[i:i+len(t)] and ck[i:i+len(t)] == [False] * len(t):
        count += 1
        ck[i:i + len(t)] = [True] * len(t)
print(count)