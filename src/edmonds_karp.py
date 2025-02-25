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
    
    # Create a deep copy of the graph to use as the residual graph
    def deep_copy_graph(g):
        return {node: g[node].copy() for node in g}
    
    residual_graph = deep_copy_graph(graph)
    
    # Ensure reciprocal edges are initialized
    for node in graph:
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
        visited = set()
        queue = deque([source])
        visited.add(source)
        
        while queue:
            current = queue.popleft()
            
            # Check neighbors
            for neighbor, capacity in residual_graph[current].items():
                if neighbor not in visited and capacity > 0:
                    parent[neighbor] = current
                    
                    # Found path to sink
                    if neighbor == sink:
                        # Find the minimum flow along the path
                        path_flow = float('inf')
                        v = sink
                        while v != source:
                            u = parent[v]
                            path_flow = min(path_flow, residual_graph[u][v])
                            v = u
                        
                        # Update residual graph
                        v = sink
                        while v != source:
                            u = parent[v]
                            residual_graph[u][v] -= path_flow
                            
                            # Ensure reverse edge exists before updating
                            if u not in residual_graph[v]:
                                residual_graph[v][u] = 0
                            residual_graph[v][u] += path_flow
                            
                            v = u
                        
                        # Add to max flow
                        max_flow += path_flow
                        
                        # Stop BFS
                        queue.clear()
                        break
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        # If no path to sink found, we're done
        if sink not in parent:
            break
    
    return max_flow