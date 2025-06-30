import math

length = int(input())
width = int(input())
height = int(input())
bottle_volume = int(input())

ans = (length * width * height) / bottle_volume
print(math.ceil(ans))