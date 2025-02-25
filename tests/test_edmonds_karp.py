import pytest
from src.edmonds_karp import edmonds_karp_max_flow

# Define sink as a constant
SINK = 'sink'

def test_simple_max_flow():
    # Simple graph with known max flow
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {SINK: 10},
        4: {3: 6, SINK: 10},
        SINK: {}
    }
    assert edmonds_karp_max_flow(graph, 0, SINK) == 10

def test_disconnected_graph():
    # Graph where source and sink are disconnected
    graph = {
        0: {},
        1: {},
        SINK: {}
    }
    assert edmonds_karp_max_flow(graph, 0, SINK) == 0

def test_single_path_graph():
    # Simple graph with single path
    graph = {
        0: {1: 5},
        1: {SINK: 5},
        SINK: {}
    }
    assert edmonds_karp_max_flow(graph, 0, SINK) == 5

def test_complex_multi_path_graph():
    # More complex graph with multiple paths
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 1, 3: 3},
        2: {3: 2, 4: 2},
        3: {SINK: 3},
        4: {SINK: 3},
        SINK: {}
    }
    assert edmonds_karp_max_flow(graph, 0, SINK) == 5

def test_invalid_graph_type():
    # Test invalid graph type
    with pytest.raises(TypeError):
        edmonds_karp_max_flow([], 0, SINK)

def test_invalid_source_or_sink():
    # Test with source/sink not in graph
    graph = {0: {1: 5}, 1: {}}
    with pytest.raises(ValueError):
        edmonds_karp_max_flow(graph, 2, SINK)
    with pytest.raises(ValueError):
        edmonds_karp_max_flow(graph, 0, 2)

def test_zero_capacity_graph():
    # Graph with zero capacity
    graph = {
        0: {1: 0},
        1: {SINK: 0},
        SINK: {}
    }
    assert edmonds_karp_max_flow(graph, 0, SINK) == 0