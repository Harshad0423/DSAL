HIGH = 99999

class Graph:
    def __init__(self):
        self.g = []
        self.n = 0
        self.dept = []
        self.v_array = []

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

    def prims(self):
        self.v_array = [False] * self.n
        self.v_array[0] = True
        print("\nPrim's MST -> EDGE : Weight")
        n_edges = 0
        cost = 0
        while n_edges < self.n - 1:
            minimum = HIGH
            u = v = -1
            for i in range(self.n):
                if self.v_array[i]:
                    for j in range(self.n):
                        if not self.v_array[j] and self.g[i][j] < minimum:
                            minimum = self.g[i][j]
                            u, v = i, j
            if u != -1 and v != -1:
                print(f"Edge: {self.dept[u]} - {self.dept[v]} with weight {minimum}")
                cost += minimum
                self.v_array[v] = True
                n_edges += 1
        print("\nCost Of Minimum Spanning Tree Using Prim's is:", cost)


if __name__ == "__main__":
    g = Graph()
    g.initialize()
    g.display()
    g.prims()
