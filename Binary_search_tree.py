# Binary Search Tree implementation in Python

class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data: # check if the of new data exist already in the tree, if yes don't add
            return
        
        if data < self.data:
            # Add to left subtree
            if self.left:
                self.left.add_child(data) # Recursively call the add_child method to add the data to an appropriate place
            else:
                self.left = BinaryTreeNode(data)
        else:
            # Add to right subtree
            if self.right:
                self.right.add_child(data) # Recursively call the add_child method to add the data to an appropriate place
            else:
                self.right = BinaryTreeNode(data)
                
            
            
            
            
            
            
