HIGH = 99999  # Represent infinity (no edge)


class Graph:
    def __init__(self):
        self.g = []      # adjacency matrix
        self.n = 0       # number of vertices
        self.dept = []   # department (vertex) names

    # ----- Initialize adjacency matrix -----
    def initialize(self):
        self.n = int(input("Enter number of departments: "))
        print("\nEnter department names:")
        for i in range(self.n):
            name = input(f"-> ")
            self.dept.append(name)

        self.g = [[0] * self.n for _ in range(self.n)]

        print("\nEnter distance between departments (0 if no direct path):")
        for i in range(self.n):
            for j in range(i + 1, self.n):
                dist = int(input(f"Distance between '{self.dept[i]}' and '{self.dept[j]}' : "))
                if dist == 0:
                    self.g[i][j] = HIGH
                    self.g[j][i] = HIGH
                else:
                    self.g[i][j] = dist
                    self.g[j][i] = dist

    # ----- Display adjacency matrix -----
    def display(self):
        print("\nAdjacency Matrix:")
        print("\t", end="")
        for name in self.dept:
            print(name, end="\t")
        print()

        for i in range(self.n):
            print(self.dept[i], end="\t")
            for j in range(self.n):
                if self.g[i][j] == HIGH:
                    print("∞", end="\t")
                else:
                    print(self.g[i][j], end="\t")
            print()

    # ----- Find function (for Disjoint Set / Union-Find) -----
    def find(self, parent, i):
        while parent[i] != i:
            i = parent[i]
        return i

    # ----- Union function (by rank) -----
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # ----- Kruskal's Algorithm -----
    def kruskal(self):
        edges = []

        # Step 1: Extract all edges from adjacency matrix
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.g[i][j] != 0 and self.g[i][j] != HIGH:
                    edges.append((self.g[i][j], i, j))

        # Step 2: Sort edges by weight
        edges.sort()

        # Step 3: Initialize disjoint sets
        parent = [i for i in range(self.n)]
        rank = [0] * self.n

        mst_edge = []
        cost = 0

        # Step 4: Process edges in increasing order
        for w, u, v in edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If adding edge doesn't cause a cycle
            if x != y:
                mst_edge.append((u, v, w))
                cost += w
                self.union(parent, rank, x, y)

        # Step 5: Display MST result
        print("\nKruskal's MST -> EDGE : Weight")
        for u, v, w in mst_edge:
            print(f"{self.dept[u]} - {self.dept[v]} : {w}")
        print("\nTotal cost of MST:", cost)


# -------- MAIN PROGRAM --------
def main():
    g = Graph()
    g.initialize()
    g.display()
    g.kruskal()


main()
