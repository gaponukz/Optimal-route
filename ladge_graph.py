from search_graph import *

ladge_graph: Graph = {
    "start": {
        "a": 5,
        "b": 2
    },
    "a": {
        "d": 4,
        "c": 2
    },
    "b": {
        "a": 8,
        "c": 7
    },
    "d": {
        "c": 6,
        "end": 2
    },
    "c": {
        "end": 1
    },
    "end": {}
}

path, cost = get_optimal_route_cost(ladge_graph)
print_path(path)
print(f"only for {cost}$")
