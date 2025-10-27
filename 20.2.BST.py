class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, key):
        current = self.root
        while current:
            if current.val == key:
                return current
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

def main():
    bst = BST()
    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Display (Inorder Traversal)")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to insert: "))
            bst.insert(val)
        elif choice == 2:
            val = int(input("Enter value to search: "))
            res = bst.search(val)
            print("Found" if res else "Not Found")
        elif choice == 3:
            print("Inorder Traversal: ", end='')
            bst.inorder(bst.root)
            print()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()
