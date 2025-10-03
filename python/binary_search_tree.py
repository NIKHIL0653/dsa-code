<<<<<<< HEAD
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# Example usage
root = None
keys = [20, 10, 30, 5, 15, 25, 35]

for key in keys:
    root = insert(root, key)

print("Inorder traversal of BST:")
inorder(root)
print()

search_key = 15
result = search(root, search_key)
if result:
    print(f"Found {search_key} in BST")
else:
    print(f"{search_key} not found in BST")
=======
from typing import Optional

class TreeNode:
    """Each node holds a value and points to left & right children"""
    def __init__(self, val):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class BinarySearchTree:
    """
    Binary Search Tree - keeps numbers organized
    Smaller values go left, larger go right
    This makes searching super fast!
    """
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    def insert(self, val) -> None:
        """Add a new number to our tree"""
        if not self.root:
            self.root = TreeNode(val)  # First node becomes the root
            return
        
        # These findes the right spot by comparing values
        current = self.root
        while True:
            if val < current.val:  # Go left for smaller values
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:  # Go right for larger values
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right
    
    def search(self, val) -> bool:
        """Check if a number exists in our tree"""
        current = self.root
        while current:
            if val == current.val:
                return True  # Found it!
            current = current.left if val < current.val else current.right
        return False  # Nope, not here
    
    def display(self, node: Optional[TreeNode] = None, level: int = 0):
        """Show the tree structure - rotated 90° to the right"""
        if node is None:
            node = self.root
        if node is None:  # Handle case where root is None
            print("Tree is empty")
            return
        if node.right:
            self.display(node.right, level + 1)
        print('    ' * level + f'→ {node.val}')
        if node.left:
            self.display(node.left, level + 1)


# Let's test it out!
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Add some numbers
    numbers = [50, 30, 70, 20, 40, 60, 80]
    print("Building tree with:", numbers)
    for num in numbers:
        bst.insert(num)
    
    # Show our tree
    print("\nTree structure:")
    bst.display()
    
    # Try searching
    print(f"\nIs 40 in tree? {bst.search(40)}")
    print(f"Is 100 in tree? {bst.search(100)}")
>>>>>>> upstream/develop
