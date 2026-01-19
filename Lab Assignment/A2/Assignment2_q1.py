# 8-Puzzle BFS without using built-in Queue or Set

# Start and Goal states (0 represents blank)
start_state = (7, 2, 4,
               5, 0, 6,
               8, 3, 1)

goal_state = (0, 1, 2,
              3, 4, 5,
              6, 7, 8)

# ---------- Custom Queue ----------
class Queue:
    def __init__(self):
        self.data = []
        self.front = 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        item = self.data[self.front]
        self.front += 1
        return item

    def is_empty(self):
        return self.front >= len(self.data)

# ---------- Custom Set ----------
class VisitedSet:
    def __init__(self):
        self.store = {}

    def add(self, item):
        self.store[item] = True

    def contains(self, item):
        return item in self.store

# Possible moves for each index of the blank tile
moves = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}

# ---------- BFS ----------
queue = Queue()
visited = VisitedSet()

queue.enqueue(start_state)
visited.add(start_state)

explored_count = 0

while not queue.is_empty():
    current = queue.dequeue()
    explored_count += 1

    if current == goal_state:
        break

    blank_index = current.index(0)

    for next_index in moves[blank_index]:
        new_state = list(current)
        new_state[blank_index], new_state[next_index] = \
            new_state[next_index], new_state[blank_index]
        new_state = tuple(new_state)

        if not visited.contains(new_state):
            visited.add(new_state)
            queue.enqueue(new_state)

# Subtract 1 to exclude goal state itself
print("States explored before reaching goal:", explored_count - 1)
