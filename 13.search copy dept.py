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

    def copy(self, root):
        if not root:
            return None
        new_node = Node(root.val)
        new_node.left = self.copy(root.left)
        new_node.right = self.copy(root.right)
        return new_node

    def height(self, node):
        if node is None:
            return -1
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

def main():
    bst = BST()
    while True:
        print("\n1. Insert\n2. Search\n3. Copy BST\n4. Display Depth\n5. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            bst.insert(int(input("Enter value: ")))
        elif ch == 2:
            val = int(input("Enter value to search: "))
            print("Found" if bst.search(val) else "Not Found")
        elif ch == 3:
            new_bst = BST()
            new_bst.root = bst.copy(bst.root)
            print("Copied BST (Inorder):", end=' ')
            new_bst.inorder(new_bst.root); print()
        elif ch == 4:
            print("Depth of Tree:", bst.height(bst.root))
        elif ch == 5:
            break
        else:
            print("Invalid choice")

main()
