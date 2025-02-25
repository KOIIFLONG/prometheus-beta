import math
from typing import List, Tuple

def find_closest_points(points_a: List[Tuple[float, float]], 
                        points_b: List[Tuple[float, float]]) -> Tuple[Tuple[Tuple[float, float], Tuple[float, float]], float]:
    """
    Find the two closest points, one from list A and one from list B, 
    using Euclidean distance.
    
    Args:
        points_a (List[Tuple[float, float]]): First list of points
        points_b (List[Tuple[float, float]]): Second list of points
    
    Returns:
        Tuple containing:
        - Tuple of the two closest points (point from A, point from B)
        - The minimum distance between these points
    
    Raises:
        ValueError: If either input list is empty
    """
    # Validate input
    if not points_a or not points_b:
        raise ValueError("Both point lists must be non-empty")
    
    # Initialize minimum distance to a large value
    min_distance = float('inf')
    closest_pair = None
    
    # Compare every point in A with every point in B
    for point_a in points_a:
        for point_b in points_b:
            # Calculate Euclidean distance
            distance = math.sqrt(
                (point_a[0] - point_b[0])**2 + 
                (point_a[1] - point_b[1])**2
            )
            
            # Update minimum distance if current distance is smaller
            # If distances are equal, prefer points with smaller coordinate values
            if (distance < min_distance or 
                (distance == min_distance and 
                 (point_a[0] + point_a[1] < closest_pair[0][0] + closest_pair[0][1] or
                  point_b[0] + point_b[1] < closest_pair[1][0] + closest_pair[1][1]))):
                min_distance = distance
                closest_pair = (point_a, point_b)
    
    return closest_pair, min_distance