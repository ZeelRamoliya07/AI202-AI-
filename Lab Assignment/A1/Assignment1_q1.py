from collections import deque

graph = {
    'Syracuse': {'Buffalo': 150, 'Philadelphia': 253, 'New York': 254, 'Boston': 312},
    'Buffalo': {'Syracuse': 150, 'Detroit': 256, 'Cleveland': 189, 'Pittsburgh': 215},
    'Detroit': {'Buffalo': 256, 'Cleveland': 169, 'Chicago': 283},
    'Cleveland': {'Buffalo': 189, 'Detroit': 169, 'Chicago': 345, 'Columbus': 144, 'Pittsburgh': 134},
    'Pittsburgh': {'Buffalo': 215, 'Cleveland': 134, 'Columbus': 185, 'Philadelphia': 305, 'Baltimore': 247},
    'Philadelphia': {'Syracuse': 253, 'Pittsburgh': 305, 'New York': 97, 'Baltimore': 101},
    'New York': {'Syracuse': 254, 'Philadelphia': 97, 'Providence': 181, 'Boston': 215},
    'Columbus': {'Cleveland': 144, 'Pittsburgh': 185, 'Indianapolis': 176},
    'Indianapolis': {'Columbus': 176, 'Chicago': 182},
    'Chicago': {'Detroit': 283, 'Cleveland': 345, 'Indianapolis': 182},
    'Boston': {'Syracuse': 312, 'New York': 215, 'Portland': 107, 'Providence': 50},
    'Providence': {'Boston': 50, 'New York': 181},
    'Portland': {'Boston': 107},
    'Baltimore': {'Pittsburgh': 247, 'Philadelphia': 101}
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
['Syracuse', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 689
['Syracuse', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 684
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 920
['Syracuse', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 791
['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 844
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1037
['Syracuse', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 841
['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 951
['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1039
['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 908
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1312
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1307
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1144
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1232
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1101
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1080
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1135
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1077
['Syracuse', 'Buffalo', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1016
['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1001
['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1146
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1543
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1414
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1420
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1194
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1339
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1355
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1350
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1187
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1275
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1144
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1410   
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1405 
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1242 
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1330
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1199
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1178
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1408  
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1252
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1464
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1615
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1586
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1457
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1463
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1237
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1382
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1641
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1512
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1518
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1292
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1437
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1453
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1448
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1285
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1373
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1242
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1683
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1678
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1515
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1603
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1472
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1451
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1424
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1700
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1507
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1658
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1562
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1713
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1684
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1555
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1561
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1335
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1480
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1914
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1785
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1791
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1565
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1710
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1726
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1721
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1558
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1646
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1515
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1699
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1694
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1531
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1619
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1488
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1467
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1743
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1798
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1605
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1756
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1835
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1986
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1957
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1828
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1834
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1608
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1753
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1930
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1801
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1807
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1581
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1726
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1742
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1737
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1574
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1662
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1531
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1841
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 2071
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1878
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 2029
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1851
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 2002
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1973
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1844
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1850
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1624
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1769
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 2114
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 2087
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1894
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 2045
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 2130

====== DFS Paths and Costs ======
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1531
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1662
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1769
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 2045
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1624
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1467
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1574
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1850
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1894
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1737
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1844
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1742
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 2130
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1973
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1488
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1619
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1726
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 2002
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1581
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1424
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1531
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1807
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1851
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1694
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1801
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1699
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 2087
['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1930
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1515
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1646
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1753
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 2029
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1608
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1451
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1558
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1834
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1878
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1721
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1828
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1726
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 2114
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1957
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1472
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1603
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1710
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1986
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1565
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1408  
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1515
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1791
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1835
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1678
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1785
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1683
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 2071
['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1914
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1242
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1373
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1480
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1756
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1335
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1178
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1285
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1561
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1605
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1448
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1555
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1453
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1841
['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1684
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1199
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1330
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1437
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1713
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1292
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1135
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1242 
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1518
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1562
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1405 
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1512
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1410   
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1798
['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1641
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1144
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1275
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1382
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1658
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1237
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1080
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1187
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1463
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1507
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1350
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1457
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1355  
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1743
['Syracuse', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1586
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1101
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1232
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1339 
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1615
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1194
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 1037
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1144
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1420  
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1464
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 1307
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1414  
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 1312
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1700
['Syracuse', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 1543  
['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 908
['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago']  -> cost = 1039
['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 1146      
['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1001 
['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Chicago']  -> cost = 844
['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 951
['Syracuse', 'Buffalo', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1016 
['Syracuse', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 841
['Syracuse', 'Buffalo', 'Cleveland', 'Chicago']  -> cost = 684
['Syracuse', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago']  -> cost = 791
['Syracuse', 'Buffalo', 'Detroit', 'Chicago']  -> cost = 689
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1252
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago']  -> cost = 1077    
['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago']  -> cost = 920"""