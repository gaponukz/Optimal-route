infinity = float("inf")
Graph = dict[str, dict[str, int]]

def _find_lowest_cost_node(costs: dict, processed: list) -> str:
    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    
    return lowest_cost_node

def get_optimal_route_cost(graph: Graph) -> int:
    processed = []

    costs = {
        point: (graph["start"][point] if point in graph["start"].keys() else infinity) 
        for point in list(graph)[1:]
    }

    node = _find_lowest_cost_node(costs, [])

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
        
        processed.append(node)
        node = _find_lowest_cost_node(costs, processed)
    
    return costs['end']
