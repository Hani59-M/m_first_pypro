import random

def is_arg(arg, prefr):
    n = len(arg)
    for i in range(n):
        guest = arg[i]
        left = arg[(i - 1) % n]
        right = arg[(i + 1) % n]
        if left not in prefr[guest] or right not in prefr[guest]:
            return False
    return True

def seating_arg(prefr, max=10000):
    guests = list(prefr.keys())
    for _ in range(max):
        random.shuffle(guests)
        if is_arg(guests, prefr):
            return guests.copy()
    return None

prefr = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['D', 'A'],
    'D': ['B', 'C']
}

result = seating_arg(prefr)
if result:
    print("seating arrangement found:", result)
else:
    print("No valid arrangement possible.")
