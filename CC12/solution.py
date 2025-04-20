# ------------------------------------------
# Problem 1: Dijkstra's Algorithm
# ------------------------------------------

class MinHeap:
    """
    MinHeap data structure supporting (vertex, distance) pairs or Node objects with estimated distances.
    Used by both Dijkstra's and A* algorithms.
    """

    def __init__(self, array):
        self.vertex_map = {idx: idx for idx in range(len(array))}
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx][1] < heap[child_one_idx][1]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx

            if heap[idx_to_swap][1] < heap[current_idx][1]:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx][1] < heap[parent_idx][1]:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def remove(self):
        if self.is_empty():
            return
        self.swap(0, len(self.heap) - 1, self.heap)
        vertex, distance = self.heap.pop()
        self.vertex_map.pop(vertex)
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return vertex, distance

    def swap(self, i, j, heap):
        self.vertex_map[heap[i][0]] = j
        self.vertex_map[heap[j][0]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def update(self, vertex, value):
        self.heap[self.vertex_map[vertex]] = (vertex, value)
        self.sift_up(self.vertex_map[vertex], self.heap)


def dijkstras_algorithm(start, edges):
    """
    Implements Dijkstra's algorithm for finding the shortest path from a start vertex
    to all other vertices in a directed graph with non-negative weights.

    Args:
        start (int): The start vertex index.
        edges (List[List[List[int]]]): Adjacency list of the graph.

    Returns:
        List[int]: Shortest distances from start to each vertex; -1 if unreachable.
    """
    pass


# ------------------------------------------
# Problem 2: A* Search Algorithm
# ------------------------------------------

class Node:
    """
    Represents a node in a grid for A* algorithm, storing coordinates, value (0 or 1),
    and distance estimates.
    """

    def __init__(self, row, col, value):
        self.id = f"{row}-{col}"
        self.row = row
        self.col = col
        self.value = value
        self.distance_from_start = float("inf")
        self.estimated_distance_to_end = float("inf")
        self.came_from = None


def a_star_algorithm(start_row, start_col, end_row, end_col, graph):
    """
    Implements the A* search algorithm to find the shortest path in a grid from a start
    node to an end node, avoiding obstacles.

    Args:
        start_row (int): Starting row index.
        start_col (int): Starting column index.
        end_row (int): Ending row index.
        end_col (int): Ending column index.
        graph (List[List[int]]): Grid map with 0 as free space and 1 as obstacle.

    Returns:
        List[List[int]]: Path from start to end as list of [row, col] pairs.
    """
    pass


def reconstruct_path(end_node):
    """
    Reconstructs the path by tracing back from the end node to the start node.

    Args:
        end_node (Node): The end node.

    Returns:
        List[List[int]]: The path from start to end as [row, col] pairs.
    """
    if not end_node.came_from:
        return []

    path = []
    current = end_node
    while current is not None:
        path.append([current.row, current.col])
        current = current.came_from

    return path[::-1]


def calculate_manhattan_distance(current, end):
    """
    Calculates the Manhattan distance between two nodes in the grid.

    Args:
        current (Node): Current node.
        end (Node): Destination node.

    Returns:
        int: Manhattan distance.
    """
    return abs(current.row - end.row) + abs(current.col - end.col)


def initialize_nodes(graph):
    """
    Converts a grid into a 2D matrix of Node objects.

    Args:
        graph (List[List[int]]): Grid of 0s and 1s.

    Returns:
        List[List[Node]]: Matrix of Node instances.
    """
    nodes = []
    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))
    return nodes


def get_neighboring_nodes(node, nodes):
    """
    Returns all 4-directional neighbors of the given node that are within bounds.

    Args:
        node (Node): The node to get neighbors for.
        nodes (List[List[Node]]): 2D grid of Node objects.

    Returns:
        List[Node]: Valid neighboring nodes.
    """
    neighbors = []
    row, col = node.row, node.col
    num_rows = len(nodes)
    num_cols = len(nodes[0])

    if row < num_rows - 1:
        neighbors.append(nodes[row + 1][col])  # Down
    if row > 0:
        neighbors.append(nodes[row - 1][col])  # Up
    if col < num_cols - 1:
        neighbors.append(nodes[row][col + 1])  # Right
    if col > 0:
        neighbors.append(nodes[row][col - 1])  # Left

    return neighbors


# Extension to MinHeap for A* (Node-based)
class AStarMinHeap:
    """
    MinHeap data structure supporting (vertex, distance) pairs or Node objects with estimated distances.
    Used by both Dijkstra's and A* algorithms.
    """

    def __init__(self, array):
        self.node_positions = {node.id: idx for idx, node in enumerate(array)}
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx].estimated_distance_to_end < heap[
                child_one_idx].estimated_distance_to_end:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx

            if heap[idx_to_swap].estimated_distance_to_end < heap[current_idx].estimated_distance_to_end:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx].estimated_distance_to_end < heap[
            parent_idx].estimated_distance_to_end:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def remove(self):
        if self.is_empty():
            return None
        self.swap(0, len(self.heap) - 1, self.heap)
        node = self.heap.pop()
        del self.node_positions[node.id]
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return node

    def insert(self, node):
        self.heap.append(node)
        self.node_positions[node.id] = len(self.heap) - 1
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        self.node_positions[heap[i].id] = j
        self.node_positions[heap[j].id] = i
        heap[i], heap[j] = heap[j], heap[i]

    def contains_node(self, node):
        return node.id in self.node_positions

    def update(self, node):
        self.sift_up(self.node_positions[node.id], self.heap)
