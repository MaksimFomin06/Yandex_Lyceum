import requests
import sys


def get_century_start(century):
    return (century - 1) * 100


def main():
    host = sys.stdin.readline().strip()
    genie = sys.stdin.readline().strip()
    century = int(sys.stdin.readline().strip())
    
    url = f"http://{host}:8080"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        return
    
    min_year = get_century_start(century)
    
    place_events = {}
    
    for entry in data:
        if entry['genie'] == genie and entry['year'] >= min_year:
            place = entry['place']
            event = entry['event']
            if place not in place_events:
                place_events[place] = set()
            place_events[place].add(event)
    
    sorted_places = sorted(place_events.keys(), reverse=True)
    
    for place in sorted_places:
        events = sorted(place_events[place])
        events_str = " . ".join(events)
        print(f"{place}: {events_str}")


if __name__ == "__main__":
    main()