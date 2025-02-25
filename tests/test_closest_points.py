import pytest
import math
from src.closest_points import find_closest_points

def test_basic_case():
    """Test with simple point lists"""
    points_a = [(0, 0), (1, 1), (3, 3)]
    points_b = [(2, 2), (4, 4), (5, 5)]
    
    closest, distance = find_closest_points(points_a, points_b)
    
    # The closest points should be (1, 1) and (2, 2)
    assert closest == ((1, 1), (2, 2))
    assert math.isclose(distance, math.sqrt(2), rel_tol=1e-9)

def test_multiple_minimum_distances():
    """Test case where multiple point pairs have the same minimum distance"""
    points_a = [(0, 0), (1, 1), (2, 2)]
    points_b = [(1, 1), (2, 2), (3, 3)]
    
    closest, distance = find_closest_points(points_a, points_b)
    
    # Should return the first pair found with minimum distance
    assert closest in [((1, 1), (1, 1)), ((2, 2), (2, 2))]
    assert math.isclose(distance, 0, rel_tol=1e-9)

def test_empty_list_raises_error():
    """Test that empty lists raise a ValueError"""
    with pytest.raises(ValueError, match="Both point lists must be non-empty"):
        find_closest_points([], [(1, 1)])
    
    with pytest.raises(ValueError, match="Both point lists must be non-empty"):
        find_closest_points([(1, 1)], [])

def test_large_distance():
    """Test with points far apart"""
    points_a = [(0, 0), (10, 10)]
    points_b = [(100, 100), (200, 200)]
    
    closest, distance = find_closest_points(points_a, points_b)
    
    # Verify the distance and that points are from different lists
    assert len(closest) == 2
    assert closest[0] in points_a
    assert closest[1] in points_b
    
    # Compute the expected distance
    expected_distance = math.sqrt(
        (closest[0][0] - closest[1][0])**2 + 
        (closest[0][1] - closest[1][1])**2
    )
    
    assert math.isclose(distance, expected_distance, rel_tol=1e-9)

def test_floating_point_coordinates():
    """Test with floating point coordinates"""
    points_a = [(0.1, 0.2), (1.5, 2.5)]
    points_b = [(0.3, 0.4), (2.5, 3.5)]
    
    closest, distance = find_closest_points(points_a, points_b)
    
    # Verify the result is one of the valid minimal distance pairs
    assert distance == pytest.approx(
        math.sqrt((0.1 - 0.3)**2 + (0.2 - 0.4)**2), 
        rel=1e-9
    )