# Type-1

import random

# Environment
rooms = {'A': 'Dirt', 'B': 'Dirt', 'C': 'Dirt'}
location = 'A'

# Rule table
rule_table = {
    ('A', 'Dirt'): ['Remove'],
    ('A', 'No Dirt'): ['Move Right'],
    ('B', 'Dirt'): ['Remove'],
    ('B', 'No Dirt'): ['Move Left', 'Move Right'],
    ('C', 'Dirt'): ['Remove'],
    ('C', 'No Dirt'): ['Move Left']
}

# Movement function
def move(loc, action):
    if loc == 'A' and action == 'Move Right': return 'B'
    if loc == 'B' and action == 'Move Left': return 'A'
    if loc == 'B' and action == 'Move Right': return 'C'
    if loc == 'C' and action == 'Move Left': return 'B'
    return loc

# Performance measure
total_cost = 0

# Cost values
CLEAN_COST = 10
MOVE_COST = 1

print("Percept\t\tAction\t\tLocation\tCost")
print("------------------------------------------------------------")

for i in range(15):
    status = rooms[location]
    actions = rule_table[(location, status)]
    action = random.choice(actions)

    step_cost = 0

    if action == 'Remove':
        rooms[location] = 'No Dirt'
        step_cost = CLEAN_COST
        print(f"({location},{status})\t{action}\t\t{location}\t\t{step_cost}")
    else:
        new_location = move(location, action)
        location = new_location
        step_cost = MOVE_COST
        print(f"({location},{status})\t{action}\t{location}\t\t{step_cost}")

    total_cost += step_cost

print("\nFinal Performance Measure")
print("-------------------------")
print("Total Cost (Utility):", total_cost)


# Type-2 : user can give percepts
# import random

# def vacuum_agent(location, status):
#     if status == "Dirt":
#         return "Remove"

#     if location == "A":
#         return "Move Right"

#     if location == "C":
#         return "Move Left"

#     if location == "B":
#         return random.choice(["Move Left", "Move Right"])


# steps = int(input("Enter number of steps: "))

# print("\nPercept\t\tAction")
# print("-------------------------------")

# for _ in range(steps):
#     location = input("Enter Location (A/B/C): ")
#     status = input("Enter Status (Dirt/No Dirt): ")

#     action = vacuum_agent(location, status)
#     print(f"({location}, {status})\t{action}")