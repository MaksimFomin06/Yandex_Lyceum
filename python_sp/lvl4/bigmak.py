from collections import defaultdict


def process_orders(input_file, output_file):
    dish_counts = defaultdict(int)
    
    with open(input_file, 'r') as f:
        current_order = []
        for line in f:
            line = line.strip()
            if line == '-' * 10:
                for dish in current_order[1:]:
                    dish_counts[dish] += 1
                current_order = []
            else:
                current_order.append(line)
        
        if current_order:
            for dish in current_order[1:]:
                dish_counts[dish] += 1
    
    sorted_dishes = sorted(dish_counts.items(), key=lambda x: (-x[1], x[0]))
    
    with open(output_file, 'w') as f:
        f.write("no,dish,quantity\n")
        for i, (dish, quantity) in enumerate(sorted_dishes, 1):
            f.write(f"{i},{dish},{quantity}\n")


process_orders("orders.txt", "waiting.csv")