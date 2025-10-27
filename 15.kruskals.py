HIGH = 99999

class Graph:
    def __init__(self):
        self.g = []
        self.n = 0
        self.dept = []

    def initialize(self):
        self.n = int(input("Enter number of departments: "))
        self.dept = []
        print("\nEnter Name Of The Department: ")
        for i in range(self.n):
            name = input()
            self.dept.append(name)
        self.g = [[0] * self.n for _ in range(self.n)]
        print("\nEnter The Distance Between Departments (0 if no path): ")
        for i in range(self.n):
            for j in range(i, self.n):
                if i == j:
                    self.g[i][j] = 0
                else:
                    dist = int(input(f"Distance Between {self.dept[i]} and {self.dept[j]}: "))
                    if dist == 0:
                        self.g[i][j] = HIGH
                        self.g[j][i] = HIGH
                    else:
                        self.g[i][j] = dist
                        self.g[j][i] = dist

    def display(self):
        print(" ", end="\t\t\t\t\t")
        for i in range(self.n):
            print(self.dept[i], end="\t\t\t\t")
        print()
        for i in range(self.n):
            print(self.dept[i], end="\t\t\t\t")
            for j in range(self.n):
                print(self.g[i][j], end="\t\t\t\t")
            print()

    def find(self, parent, i):
        while parent[i] != i:
            i = parent[i]
        return i

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

    def kruskals(self):
        edges = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.g[i][j] != 0 and self.g[i][j] != HIGH:
                    edges.append((self.g[i][j], i, j))
        edges.sort()
        parent = [i for i in range(self.n)]
        rank = [0] * self.n
        mst_edges = []
        cost = 0
        for w, u, v in edges:
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                mst_edges.append((u, v, w))
                cost += w
                self.union(parent, rank, x, y)
        print("\nKruskal's MST -> EDGE : Weight")
        for u, v, w in mst_edges:
            print(f"{self.dept[u]} - {self.dept[v]} : {w}")
        print("\nCost of minimum spanning tree using Kruskal's:", cost)


if __name__ == "__main__":
    g = Graph()
    g.initialize()
    g.display()
    g.kruskals()
