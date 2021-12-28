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
    
    
    def in_order_traversal(self): # Visit Left subtree, then Root node and finaly Right subtree
        elements = []
        
        # Getting all elements of the Left Subtree    
        if self.left:
            elements += self.left.in_order_traversal() # Recursively get all the elements of the left subtree and add them into the list
        elements.append(self.data) # Adding the root node to the list
        
        # Getting all elements of the Right Subtree    
        if self.right:
            elements += self.right.in_order_traversal() # Recursively get all the elements of the right subtree and add them into the list
        return elements
    
# Tree Builder helper method
def build_binary_tree(lst_elem: list):
    if len(lst_elem) >1:
        root_node = BinaryTreeNode(lst_elem[0])
        for i in lst_elem[1:]:
            root_node.add_child(i)
    
        return print(root_node.in_order_traversal())
    else:
        return print("Insufficient number of elements")
        

if __name__ == '__main__':
   elems = [17, 4, 1, 20, 9, 23, 18, 34]
   build_binary_tree(elems)
            
            
            
