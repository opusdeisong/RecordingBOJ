import sys
N = int(sys.stdin.readline())
i = 0
while True:
    if 2 ** i >= N:
        minus = 2 ** (i - 1)
        break
    i += 1
    continue
if N == 1 or N == 2:
    print(N)
else:
    print((N - minus) * 2)