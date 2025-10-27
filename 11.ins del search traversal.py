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

    def delete(self, root, key):
        if root is None:
            print("Tree is Empty.")
            return root
        parent = None
        current = root
        while current and current.val != key:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right
        if current is None:
            print(f"Key {key} not found in the tree.")
            return root
        if current.left is None and current.right is None:
            if not parent:
                return None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
            print("Deleted node:", current.val)
        elif current.left is None:
            if not parent:
                return current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
            print("Deleted node:", current.val)
        elif current.right is None:
            if not parent:
                return current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            print("Deleted node:", current.val)
        else:
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            current.val = successor.val
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
            print("Deleted node:", key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=' ')

def main():
    bst = BST()
    while True:
        print("\n1. Insert\n2. Delete\n3. Search\n4. Inorder\n5. Preorder\n6. Postorder\n7. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            bst.insert(int(input("Enter value: ")))
        elif ch == 2:
            bst.root = bst.delete(bst.root, int(input("Enter value to delete: ")))
        elif ch == 3:
            val = int(input("Enter value to search: "))
            print("Found" if bst.search(val) else "Not Found")
        elif ch == 4:
            print("Inorder:", end=' ')
            bst.inorder(bst.root); print()
        elif ch == 5:
            print("Preorder:", end=' ')
            bst.preorder(bst.root); print()
        elif ch == 6:
            print("Postorder:", end=' ')
            bst.postorder(bst.root); print()
        elif ch == 7:
            break
        else:
            print("Invalid choice")

main()
