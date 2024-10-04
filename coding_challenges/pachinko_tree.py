# Search a tree like it was a pachinko game
from typing import Optional


class Node:
    # Can't use `"Node" | None` ?
    def __init__(self, left: Optional["Node"], right: Optional["Node"], prize: bool = False):
        self.left = left
        self.right = right
        self.prize = prize
    def __str__(self):
        if self.prize:
            return "Found the prize!"
        else:
            return f"left: {self.left} - right: {self.right}"


tree = Node(
    left=Node(
        left=Node(
            left=None,
            right=None
        ),
        right=Node(
            left=None,
            right=None
        )
    ),
    right=Node(
        left=Node(
            left=None,
            right=None,
        ),
        right=Node(
            left=None,
            right=None,
            prize=True
        )
    )
)
print(tree)
import random
def search(root:Node):
    """Returns prize or None"""
    if root.prize:
        return root
    if root.left is None and root.right is None:
        return None
    flip = random.randint(0,1)
    original_root = root
    print("R", end="")
    while True:
        if flip == 0:
            print("L",end="")
            root = root.left
        else:
            print("R", end="")
            root = root.right
        if root.prize:
            print()
            return root
        if root.left is None and root.right is None:
            print()
            return search(original_root)

if __name__ == '__main__':
    print(search(tree))




