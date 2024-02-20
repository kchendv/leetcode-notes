"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def get_node(self, n):
        copy_neighbors = []
        if n.val not in self.a:
            copy_node = Node(n.val,[])
            self.a[n.val] = copy_node
            for neighbor in n.neighbors:
                copy_neighbors.append(self.get_node(neighbor))
            copy_node.neighbors = copy_neighbors
        return self.a[n.val]
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        self.a = dict()
        return self.get_node(node)