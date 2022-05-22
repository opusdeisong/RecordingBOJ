import sys
N, K = map(int, sys.stdin.readline().split())
ans = 1
for _ in range(1, K + 1):
    ans *= N
    N -= 1
    ans /= _
print(int(ans))