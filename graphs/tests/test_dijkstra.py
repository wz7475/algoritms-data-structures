from dijkstra import Dijkstra

def test_path_find():
    input_vertices = ("A", "B", "C", "D", "E", "F", "G")
    input_graph = {
        "A": {"B": 5, "D": 3, "E": 12, "F": 5},
        "B": {"A": 5, "D": 1, "G": 2},
        "C": {"E": 1, "F": 16, "G": 2},
        "D": {"A": 3, "B": 1, "E": 1, "G": 1},
        "E": {"A": 12, "C": 1, "D": 1, "F": 2},
        "F": {"A": 5, "C": 16, "E": 2},
        "G": {"B": 2, "C": 2, "D": 1}
    }
    dijkstra = Dijkstra(input_vertices, input_graph, "B", "C")
    assert dijkstra.get_paths() == ['B', 'D', 'E', 'C']
