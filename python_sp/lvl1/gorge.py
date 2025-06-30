count = int(input())
lst = list()

for i in range(count):
    lst1 = list()
    num = int(input())
    while num != 0:
        lst1.append(num)
        num = int(input())
    lst.append(lst1)

num = 1
num_mass = 0
mini = min(lst[0])
for i in lst:
    for j in i:
        if j <= mini:
            mini = j
            num_mass = num      
    num += 1

if mini < 0:
    print("Ущелье!")
else:
    print(f"Наименьшая высота {mini} в(о) {num_mass}-м массиве.")