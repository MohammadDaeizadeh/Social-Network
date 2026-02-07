# Final Project — Graph Algorithms in Real Networks
# Option B: Social Network (Facebook SNAP)
# -------------------------------------------------
# This project models a real social network as a graph and applies
# core graph algorithms implemented completely from scratch.


from collections import deque, defaultdict

# Graph Data Structure


class Graph:
    """
    Simple undirected, unweighted graph.
    Nodes represent users and edges represent friendships.
    """
    def __init__(self):
        # adjacency list: node -> set of neighbors
        self.adj = defaultdict(set)

    def add_edge(self, u, v):
        """Add an undirected edge between u and v"""
        self.adj[u].add(v)
        self.adj[v].add(u)

    def nodes(self):
        """Return all nodes in the graph"""
        return list(self.adj.keys())



# Core Graph Algorithms (Implemented From Scratch)


# Breadth-First Search

def bfs_shortest_path(graph, source):
    """
    Breadth-First Search starting from a source node.
    Computes shortest path distances (in number of hops)
    and parent pointers for path reconstruction.
    """
    dist = {source: 0}
    parent = {source: None}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in graph.adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    return dist, parent


# Connected Components (DFS)

def connected_components(graph):
    """
    Finds all connected components in the graph.
    Implemented ITERATIVELY (stack-based) to avoid Python recursion limits
    on large real-world graphs.
    """
    visited = set()
    components = []

    for start in graph.nodes():
        if start in visited:
            continue

        component = []
        stack = [start]
        visited.add(start)

        while stack:
            u = stack.pop()
            component.append(u)
            for v in graph.adj[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

        components.append(component)

    return components


# Degree Centrality

def degree_centrality(graph):
    """
    Degree centrality = number of direct friends per user.
    High-degree nodes are highly connected and influential.
    """
    return {node: len(graph.adj[node]) for node in graph.nodes()}




# Flow Network (for Matching Problems)


class FlowNetwork:
    """
    Directed graph with capacities, used for max-flow problems.
    Implemented as a residual network.
    """
    def __init__(self):
        self.capacity = defaultdict(lambda: defaultdict(int))
        self.adj = defaultdict(list)

    def add_edge(self, u, v, cap):
        """Add a directed edge with capacity cap"""
        self.capacity[u][v] += cap
        self.capacity[v][u] += 0  # reverse edge
        self.adj[u].append(v)
        self.adj[v].append(u)


# Edmonds–Karp Algorithm

def edmonds_karp(network, source, sink):
    """
    Computes the maximum flow from source to sink using
    the Edmonds–Karp algorithm (BFS-based Ford–Fulkerson).
    """
    max_flow = 0

    while True:
        parent = {source: None}
        queue = deque([source])

        # BFS to find an augmenting path
        while queue and sink not in parent:
            u = queue.popleft()
            for v in network.adj[u]:
                if v not in parent and network.capacity[u][v] > 0:
                    parent[v] = u
                    queue.append(v)

        # No augmenting path found
        if sink not in parent:
            break

        # Find bottleneck capacity
        bottleneck = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            bottleneck = min(bottleneck, network.capacity[u][v])
            v = u

        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            network.capacity[u][v] -= bottleneck
            network.capacity[v][u] += bottleneck
            v = u

        max_flow += bottleneck

    return max_flow



# Dataset Loader (Facebook SNAP)


# File format: each line contains two user IDs representing a friendship

def load_facebook_graph(file_path):
    """
    Loads the Facebook SNAP dataset into a Graph object.
    """
    graph = Graph()
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            u, v = line.strip().split()
            graph.add_edge(u, v)
    return graph



# Task 1 — Network Connectivity Analysis


def analyze_connectivity(graph, source):
    """
    Analyzes how information spreads in the social network.
    Returns connectivity and centrality statistics.
    """
    dist, _ = bfs_shortest_path(graph, source)
    components = connected_components(graph)
    centrality = degree_centrality(graph)

    return {
        "reachable_users": len(dist),
        "number_of_components": len(components),
        "largest_component_size": max(len(c) for c in components),
        "top_central_users": sorted(
            centrality.items(), key=lambda x: x[1], reverse=True
        )[:5]
    }



# Task 2 — Pair Matching Using Max-Flow


# Example: pairing users into teams or assigning volunteers to tasks

def build_matching_network(left_nodes, right_nodes, edges):
    """
    Builds a bipartite flow network for matching problems.
    """
    network = FlowNetwork()
    SOURCE = "SOURCE"
    SINK = "SINK"

    for u in left_nodes:
        network.add_edge(SOURCE, u, 1)

    for v in right_nodes:
        network.add_edge(v, SINK, 1)

    for u, v in edges:
        network.add_edge(u, v, 1)

    return network, SOURCE, SINK



# Bonus Task — Link Prediction


# Common Neighbors heuristic

def common_neighbors(graph, u, v):
    """Number of mutual friends between u and v"""
    return len(graph.adj[u] & graph.adj[v])


def link_prediction(graph, top_k=10):
    """
    Predicts missing friendships based on common neighbors.
    Returns the top-k most likely new edges.
    """
    nodes = graph.nodes()
    scores = []

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            if v not in graph.adj[u]:
                score = common_neighbors(graph, u, v)
                if score > 0:
                    scores.append((u, v, score))

    scores.sort(key=lambda x: x[2], reverse=True)
    return scores[:top_k]



# Example Usage


if __name__ == "__main__":
    graph = load_facebook_graph("facebook_combined.txt")

    # Task 1
    start_user = graph.nodes()[0]
    stats = analyze_connectivity(graph, start_user)

    print("Network Connectivity Analysis")
    for k, v in stats.items():
        print(f"{k}: {v}")

    # Task 2
    users = graph.nodes()
    left_group = users[:50]
    right_group = users[50:100]

    # Only allow matches if users are friends
    possible_pairs = [(u, v) for u in left_group for v in graph.adj[u] if v in right_group]

    network, S, T = build_matching_network(left_group, right_group, possible_pairs)
    max_matching = edmonds_karp(network, S, T)

    print("Maximum matching size:", max_matching)

    # Bonus
    predictions = link_prediction(graph)
    print("Predicted missing friendships:")
    for u, v, score in predictions:
        print(u, v, "score:", score)
