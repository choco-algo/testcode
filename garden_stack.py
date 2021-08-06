import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range (n):
    h.append(int(input()))
cnt = 0
result = []
for i in range (n):
    while result != [] and result[-1] <= h[i]:
        result.pop()
    result.append(h[i])
    cnt += len(result)-1

print(cnt)
