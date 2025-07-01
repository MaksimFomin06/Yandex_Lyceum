import sys


def process_data(input_data):
    passenger_data = {}
    lines = input_data.strip().split('\n')
    
    separator = lines.index('')
    data_lines = lines[:separator]
    query_lines = lines[separator + 1:]
    
    for line in data_lines:
        parts = list(map(int, line.split()))
        height = parts[0]
        passengers = parts[1:]
        station = (height // 100) * 100
        
        if station not in passenger_data:
            passenger_data[station] = set()
        
        for passenger in passengers:
            passenger_data[station].add(passenger)
    
    query_count = int(query_lines[0])
    queries = list(map(int, query_lines[1:1 + query_count]))
    
    results = []
    for query in queries:
        if query in passenger_data:
            sorted_passengers = sorted(passenger_data[query])
            results.append(', '.join(map(str, sorted_passengers)))
        else:
            results.append("No info")
    
    return '\n'.join(results)


input_data = sys.stdin.read()

print(process_data(input_data))