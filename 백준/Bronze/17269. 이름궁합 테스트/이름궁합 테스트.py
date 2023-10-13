n, m = map(int, input().split())
a, b = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
ab = ''
for i in range(min(len(a), len(b))):
    ab += a[i] + b[i]
ab += a[min(len(a), len(b)):] + b[min(len(a), len(b)):]

arr = [alp[ord(ab[i])-ord('A')] for i in range(len(ab))]


for i in range(len(arr)-2):
    for j in range(len(arr)-i-1):
        arr[j] += arr[j+1]
        arr[j] %= 10

print("{}%".format(arr[0]*10 + arr[1]))