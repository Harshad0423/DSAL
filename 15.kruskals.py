class Graph:
    def __init__(self, n, g):
        self.n = n
        self.g = g

    def kruskals(self):
        edges = []

        # Collect all edges
        for i in range(self.n):
            for j in range(i + 1, self.n):  # avoid duplicates
                w = self.g[i][j]
                if w != 0 and w != float('inf'):
                    edges.append((w, i, j))

        # Sort edges by weight
        edges.sort(key=lambda x: x[0])

        visited = set()
        cost = 0

        print("\nEdges in MST:")
        for w, i, j in edges:
            if i in visited and j in visited:
                continue
            print(f"{i} -- {j} == {w}")
            cost += w
            visited.add(i)
            visited.add(j)

        print("Total cost of MST:", cost)


# ---- MAIN ----
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (use 0 for no edge, and -1 for infinity):")

graph = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    # Replace -1 with infinity
    row = [float('inf') if x == -1.0 else x for x in row]
    graph.append(row)

g = Graph(n, graph)
g.kruskals()
