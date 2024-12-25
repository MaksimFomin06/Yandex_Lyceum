data = []
while True:
    line = input().strip()
    if not line:
        break
    data.append(line)

rooms = {}

for row in data:
    if row.isalpha():
        continue
    
    parts = row.rsplit(' ', maxsplit=1)
    subject = parts[0]
    room_number = int(parts[1])
    
    rooms.setdefault(room_number, []).append(subject)

sorted_rooms = sorted(rooms.keys())

ans = []
for room in sorted_rooms:
    unique_subjects = list(dict.fromkeys(rooms[room]))
    ans.append(f"{room}: {', '.join(unique_subjects)}")

print("\n".join(ans))