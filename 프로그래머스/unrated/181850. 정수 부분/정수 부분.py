import sys
sys.setrecursionlimit(10000)

from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()

def solution(flo):
    answer = int(flo)
    return answer