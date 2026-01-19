# 8-Puzzle DFS (no built-in stack or set)

start_state = (7, 2, 4,
               5, 0, 6,
               8, 3, 1)

goal_state = (0, 1, 2,
              3, 4, 5,
              6, 7, 8)

# ---------- Custom Stack ----------
class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0

# ---------- Custom Visited ----------
class VisitedSet:
    def __init__(self):
        self.store = {}

    def add(self, item):
        self.store[item] = True

    def contains(self, item):
        return item in self.store

# Move table
moves = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}

stack = Stack()
visited = VisitedSet()

stack.push((start_state, 0))
visited.add(start_state)

explored_count = 0

while not stack.is_empty():
    current, depth = stack.pop()
    explored_count += 1

    if current == goal_state:
        break

    blank = current.index(0)

    # Reverse order to simulate standard DFS expansion
    for nxt in reversed(moves[blank]):
        new_state = list(current)
        new_state[blank], new_state[nxt] = new_state[nxt], new_state[blank]
        new_state = tuple(new_state)

        if not visited.contains(new_state):
            visited.add(new_state)
            stack.push((new_state, depth + 1))

print("DFS states explored before goal:", explored_count - 1)
