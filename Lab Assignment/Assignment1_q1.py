from collections import deque

graph = {
    "Chicago": {"Detroit": 283, "Cleveland": 345, "Indianapolis": 182},
    "Detroit": {"Chicago": 283, "Cleveland": 169, "Buffalo": 256},
    "Cleveland": {"Chicago": 345, "Detroit": 169, "Buffalo": 189, "Pittsburgh": 134, "Columbus": 144},
    "Buffalo": {"Detroit": 256, "Cleveland": 189, "Syracuse": 150},
    "Syracuse": {"Buffalo": 150, "Cleveland": 215, "Pittsburgh": 253, "New York": 312, "Boston": 254},
    "Pittsburgh": {"Cleveland": 134, "Syracuse": 253, "Philadelphia": 305, "Baltimore": 247, "Columbus": 185},
    "Indianapolis": {"Chicago": 182, "Columbus": 176},
    "Columbus": {"Indianapolis": 176, "Cleveland": 144, "Pittsburgh": 185},
    "Philadelphia": {"Pittsburgh": 305, "New York": 97, "Baltimore": 101},
    "Baltimore": {"Pittsburgh": 247, "Philadelphia": 101},
    "New York": {"Philadelphia": 97, "Syracuse": 312, "Boston": 215, "Providence": 181},
    "Boston": {"New York": 215, "Syracuse": 254, "Providence": 50, "Portland": 107},
    "Providence": {"Boston": 50, "New York": 181},
    "Portland": {"Boston": 107}
}

start = "Syracuse"
goal = "Chicago"

#function to find the smallest path using BFS
def bfs_all_paths_costs(graph, start, goal):
    queue = deque([(start, [start], 0)])
    results = []

    while queue:
        node, path, cost = queue.popleft()

        if node == goal:
            results.append((path, cost))

        for neighbor, w in graph[node].items():
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor], cost + w))

    return results


#function to find the smallest path using BFS
def dfs_all_paths_costs(graph, start, goal):
    stack = [(start, [start], 0)]
    results = []

    while stack:
        node, path, cost = stack.pop()

        if node == goal:
            results.append((path, cost))

        for neighbor, w in graph[node].items():
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor], cost + w))

    return results

#Run the code
bfs_results = bfs_all_paths_costs(graph, start, goal)
dfs_results = dfs_all_paths_costs(graph, start, goal)

print("====== BFS Paths and Costs ======")
for p, c in bfs_results:
    print(p, " -> cost =", c)

print("\n====== DFS Paths and Costs ======")
for p, c in dfs_results:
    print(p, " -> cost =", c)

#Output
"""====== BFS Paths and Costs ======
['Syracuse', 'Cleveland', 'Chicago']  -> cost = 560
['Syracuse', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 689
['Syracuse', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 684
['Syracuse', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 667
['Syracuse', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 732
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 920
['Syracuse', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 791
['Syracuse', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 943
['Syracuse', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 717
['Syracuse', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 839
['Syracuse', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 796
['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 927
['Syracuse', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 841
['Syracuse', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 892
['Syracuse', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1115
['Syracuse', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 889
['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1034
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1193
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1077    
['Syracuse', 'Buffalo', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1016 
['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1310      
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1300 
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1257
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1388
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1236
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1350  
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1252
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1576
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1350
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1495
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1343
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1300
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1431
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1457
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1414
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1545
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1393
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1366
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1771
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1619
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1393
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1538
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1733
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1507
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1652
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1500
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1457
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1588
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1473
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1430
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1561
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1409
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1814
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1928
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1776
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1550
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1695
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1749
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1523
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1668
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1516
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1473
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1604
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1971
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1944
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1792
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1566
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1711
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1987

====== DFS Paths and Costs ======
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1987
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1711
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1604
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1473
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1566
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1792
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1516
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1409
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1944
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1668
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1561
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1430
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1523
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1749
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1473
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1366
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1971
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1695
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1588
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1457
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1550
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1776
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1500
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1393
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1928
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1652
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1545
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1414
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1507
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1733
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1457
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1350  
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1814
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1538
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1431
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']
  -> cost = 1300
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1393
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1619
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1343
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1236
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1771
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1495
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1388
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1257
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1350
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1576
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1300 
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1193
['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1310      
['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1034
['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 927
['Syracuse', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 796
['Syracuse', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 889
['Syracuse', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1115
['Syracuse', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 839
['Syracuse', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 732
['Syracuse', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 717
['Syracuse', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 892
['Syracuse', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 943
['Syracuse', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 667
['Syracuse', 'Cleveland', 'Chicago']  -> cost = 560
['Syracuse', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 841
['Syracuse', 'Buffalo', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1016 
['Syracuse', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 791
['Syracuse', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 684
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1077    
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1252
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 920
['Syracuse', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 689"""