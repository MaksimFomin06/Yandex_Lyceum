import csv


def find_best_items(max_budget, items):
    affordable_items = [(item['Название'], int(item['Цена'])) for item in items if int(item['Цена']) <= max_budget]
    if not affordable_items:
        return "error"
    affordable_items.sort(key=lambda x: x[1])
    if affordable_items[0][1] == max_budget:
        return affordable_items[0][0]
    dp = [0] * (max_budget + 1)
    names = [""] * (max_budget + 1)
    for name, price in affordable_items:
        for budget in range(max_budget, price - 1, -1):
            if dp[budget] < dp[budget - price] + 1:
                dp[budget] = dp[budget - price] + 1
                names[budget] = name
    result = []
    current_budget = max_budget
    while current_budget > 0:
        result.append(names[current_budget])
        current_budget -= int(items[affordable_items.index((names[current_budget],))]['Цена'])
    return ', '.join(result)


with open('wares.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';', fieldnames=['Название', 'Цена'])
    items = list(reader)

max_budget = 1000
result = find_best_items(max_budget, items)
print(result)