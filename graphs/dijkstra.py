from queue import PriorityQueue

class Dijkstra:

    def __init__(self, vertices, graph, start, end):
        self._vertices = vertices  # ("A", "B", "C" ...)
        self._graph = graph  # {"A": {"B": 1}, "B": {"A": 3, "C": 5} ...}
        self._visited = None
        self._parents = None
        self._costs = None
        self._start = start
        self._end = end
        self._process()

    def _process(self):
        self._costs = {vertice: float("inf") for vertice in self._vertices}
        self._costs[self._start] = 0  # set start vertex to 0

        unvisted_queue = PriorityQueue()
        for element in self._costs:
            unvisted_queue.put((self._costs[element], element))
        self._visited = {}  # set of all visited nodes
        self._parents = {}
        while self._costs:
            # min_vertex = min(self._costs, key=self._costs.get)  # get smallest distance
            min_vertex = unvisted_queue.get()[1]  # get smallest distance
            # key is to use not keys of self._costs (A, B, C..), but assigned to them values
            # for neighbour, _ in self.graph.get(min_vertex, {}).items():
            for neighbour in self._graph[min_vertex]:
                if neighbour in self._visited:
                    continue
                new_cost = self._costs[min_vertex] + self._graph[min_vertex][neighbour]
                if new_cost < self._costs[neighbour]:
                    self._costs[neighbour] = new_cost
                    unvisted_queue.put((self._costs[neighbour], neighbour))
                    self._parents[neighbour] = min_vertex
            self._visited[min_vertex] = self._costs[min_vertex]
            if min_vertex == self._end:
                break

    def get_paths(self):
        path = [self._end]
        while True:
            key = self._parents[path[0]]
            path.insert(0, key)
            if key == self._start:
                break
        return path



input_vertices = ("A", "B", "C", "D", "E", "F", "G")
input_graph = {
    "A": {"B": 5, "D": 3, "E": 12, "F": 5},
    "B": {"A": 5,  "G": 2},
    "C": {"E": 1, "F": 16, "G": 2},
    "D": {"A": 3, "E": 1, "G": 1},
    "E": {"A": 12, "C": 1, "D": 1, "F": 2},
    "F": {"A": 5, "C": 16, "E": 2},
    "G": {"B": 2, "C": 2, "D": 1}
}
start_vertex = "B"
end_vertex = "C"

dijkstra = Dijkstra(input_vertices, input_graph, start_vertex, end_vertex)
print(dijkstra.get_paths())
# parents, visted = dijkstra.find_route(start_vertex, end_vertex)
#
# print("Distance from %s to %s is: %.2f" % (start_vertex, end_vertex, visted[end_vertex]))
# se = dijkstra.generate_path(parents, start_vertex, end_vertex)
# print("Path from %s to %s is: %s" % (start_vertex, end_vertex, " -> ".join(se)))
