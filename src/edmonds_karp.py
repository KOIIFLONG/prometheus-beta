from typing import List, Dict, Optional
from collections import deque

def edmonds_karp_max_flow(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Edmonds-Karp algorithm to find the maximum flow in a network.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph.
                                           Keys are nodes, values are dictionaries of 
                                           {destination_node: edge_capacity}
        source (int): Source node
        sink (int): Sink node
    
    Returns:
        int: Maximum flow from source to sink
    
    Raises:
        ValueError: If source or sink nodes are not in the graph
        TypeError: If graph is not a valid format
    """
    # Validate input
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")
    
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph (deep copy to avoid modifying original)
    residual_graph = {}
    for node in graph:
        residual_graph[node] = graph[node].copy()
        
        # Initialize reciprocal edges with 0 if not existing
        for neighbor in graph[node]:
            if neighbor not in residual_graph:
                residual_graph[neighbor] = {}
            if node not in residual_graph[neighbor]:
                residual_graph[neighbor][node] = 0
    
    # Initialize max flow
    max_flow = 0
    
    # Find augmenting paths using BFS
    while True:
        # Perform BFS to find an augmenting path
        parent = {}
        min_capacity = {}
        visited = set()
        queue = deque([source])
        visited.add(source)
        min_capacity[source] = float('inf')
        
        while queue:
            current = queue.popleft()
            
            # Check neighbors
            for neighbor, capacity in residual_graph[current].items():
                if neighbor not in visited and capacity > 0:
                    # Update path flow
                    path_flow = min(min_capacity[current], capacity)
                    min_capacity[neighbor] = path_flow
                    parent[neighbor] = current
                    
                    # Found path to sink
                    if neighbor == sink:
                        max_flow += path_flow
                        
                        # Update residual graph
                        v = sink
                        while v != source:
                            u = parent[v]
                            residual_graph[u][v] -= path_flow
                            residual_graph[v][u] += path_flow
                            v = u
                        
                        queue.clear()
                        break
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        # If no path to sink found, we're done
        if sink not in parent:
            break
    
    return max_flow