from search_graph import *

graph: Graph = {
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

path, cost = get_optimal_route_cost(graph)
print_path(path)
print(f"only for {cost}$")
