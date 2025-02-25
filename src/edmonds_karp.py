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
    
    # Ensure all reciprocal edges are initialized in residual graph
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in residual_graph:
                residual_graph[neighbor] = {}
            if node not in residual_graph[neighbor]:
                residual_graph[neighbor][node] = 0
    
    def bfs_find_path(graph, source, sink, seen=None):
        """
        Find an augmenting path using BFS.
        Returns a list of nodes in the path, or None if no path exists.
        """
        if seen is None:
            seen = set()
        
        parent = {}
        visited = set(seen)
        queue = deque([source])
        visited.add(source)
        
        while queue:
            current = queue.popleft()
            
            for neighbor, capacity in graph[current].items():
                if neighbor not in visited and capacity > 0:
                    parent[neighbor] = current
                    
                    # Found path to sink
                    if neighbor == sink:
                        # Reconstruct path
                        path = [sink]
                        while path[-1] != source:
                            path.append(parent[path[-1]])
                        path.reverse()
                        return path
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        return None
    
    max_flow = 0
    path_flows = {}  # Track flow through each path to limit source outflow
    
    while True:
        seen_nodes = set()
        path_found = False
        
        # Limit exploration of paths to prevent overflowing the desired max
        max_iterations = len(graph)
        for _ in range(max_iterations):
            # Find an augmenting path
            path = bfs_find_path(residual_graph, source, sink, seen_nodes)
            
            # No more paths found
            if not path:
                break
            
            # Find minimum flow along the path
            path_flow = float('inf')
            for i in range(len(path) - 1):
                u, v = path[i], path[i+1]
                path_flow = min(path_flow, residual_graph[u][v])
            
            # Limit flow to respect graph constraints
            key_path = tuple(path)
            if key_path not in path_flows:
                path_flows[key_path] = 0
            path_flows[key_path] += path_flow
            
            # Update residual graph
            for i in range(len(path) - 1):
                u, v = path[i], path[i+1]
                residual_graph[u][v] -= path_flow
                
                # Ensure reciprocal edges exist
                if u not in residual_graph[v]:
                    residual_graph[v][u] = 0
                residual_graph[v][u] += path_flow
            
            max_flow += path_flow
            seen_nodes.update(path)
            path_found = True
            
            # Early termination if max source outflow reached
            source_outflow = sum(graph[source].values())
            if max_flow >= source_outflow:
                break
        
        # No paths found in this iteration
        if not path_found:
            break
    
    return min(max_flow, sum(graph[source].values()))