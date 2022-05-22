import sys
T = int(sys.stdin.readline())
for _ in range(T):
    PS = list(sys.stdin.readline())
    ans = 0
    for i in PS:
        if i == "(":
            ans += 1
        elif i == ")":
            ans -= 1
        if ans < 0:
            print("NO")
            break
    if ans > 0:
        print("NO")
    elif ans == 0:
        print("YES")