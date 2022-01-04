# Find optimal route with Bellman–Ford algorithm
About algorithm https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm

Problem: find optimal route in graph

![image](https://user-images.githubusercontent.com/49754258/148105476-99894a36-aa97-4efc-99d2-ebd53c186737.png)
```python
graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "a": {
        "end": 1
    },
    "b": {
        "a": 3,
        "end": 5
    },
    "end": {}
}

costs = {
    'a': 6, 
    'b': 2, 
    'end': inf
}
```
Realization
```python
processed = []
node = find_lowest_cost_node(costs, [])

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
    
    processed.append(node)
    node = find_lowest_cost_node(costs, processed)
```
Find a cheap way function
```python
def find_lowest_cost_node(costs: dict, processed: list):
    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    
    return lowest_cost_node
```

Then try for ladger graph (in search_ladge_graph.py file)
![image](https://user-images.githubusercontent.com/49754258/148109939-86f39df2-a34c-4b22-8437-6e1b2648a65b.png)
