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

print(get_optimal_route_cost(graph))
