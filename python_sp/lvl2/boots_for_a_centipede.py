shoes = list(input().split())
count = int(input())

now_shoes = 0
num_shoes = 1

for i in range(count):
    if i == count - 1:
        print(f"{num_shoes}-я пара ножек: {shoes[now_shoes].lower()}.")
    else:
        print(f"{num_shoes}-я пара ножек: {shoes[now_shoes].lower()};")
            
    now_shoes += 1
    num_shoes += 1
    
    if now_shoes == len(shoes):
        now_shoes = 0