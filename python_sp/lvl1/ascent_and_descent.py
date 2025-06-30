start = int(input())
startt = start
top = int(input())
step = int(input())
ans = []

while start < top:
    ans.append(start)
    start += step

while top >= startt:
    ans.append(top)
    top -= step + 1

print(*ans, sep=" ")