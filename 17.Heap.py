class Heap:
    def __init__(self):
        self.arr = []

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1   # left child
        right = 2 * i + 2  # right child

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left
        if right < n and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]  # Swap
            self.heapify(n, largest)

    def build_max_heap(self):
        n = len(self.arr)
        # Start from last non-leaf node and heapify each node
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

    def heapSort(self):
        n = len(self.arr)
        self.build_max_heap()
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]  # Swap root with last element
            self.heapify(i, 0)

    def display(self):
        for i in range(len(self.arr)):
            print(self.arr[i], end=' ')
        print()

# Main function to execute heap sort
if __name__ == "__main__":
    heap = Heap()
    n = int(input("Enter number of elements: "))
    print("Enter the elements:")
    for _ in range(n):
        element = int(input())
        heap.arr.append(element)
    print("Array before sorting:")
    heap.display()
    heap.heapSort()
    print("Array after sorting:")
    heap.display()
