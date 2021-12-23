# Implementation of Trees in Python

class TreeNode(): # Recursive data structure inwhich each Node could be a tree itself
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
        
        
    # Add children or sub-nodes to the tree
    def add_child(self, child): # child node is being added to a parent node which itself is an instance of the TreeNode Class
        child.parent = self # child is an instance of the TreeNode class and has a property/attribute parent and I am setting it to the current instance 
        self.children.append(child)
        
        
        
        
        
def build_tree():
    root = TreeNode("Electronics") #Creating a root node with data = "Electronic"
    
    laptop = TreeNode("Laptop") # Creating a parent Node with data = "Laptop"
    
    # Add children or leaf nodes to the parent Laptop
    laptop.add_child("Apple")
    laptop.add_child("Toshiba")
    laptop.add_child("HP")
    
    
    cell_phone = TreeNode("Cell Phone") # Creating a parent Node with data = "Cell Phone"
    
    # Add children or leaf nodes to the parent Cell Phone
    cell_phone.add_child("iPhone")
    cell_phone.add_child("Samsung")
    cell_phone.add_child("Huawei")

    
    tv = TreeNode("TV") # Creating a parent Node with data = "TV"
    
    # Add children or leaf nodes to the parent TV
    tv.add_child("LG")
    tv.add_child("Samsung")
    tv.add_child("Phillips")
    
    
    root.add_child(laptop) # Adding a parent node, "Laptop" to the root Node
    root.add_child(cell_phone) # Adding a parent node, "Cell Phone" to the root Node
    root.add_child(tv) # Adding a parent node, "TV" to the root Node
    
    return root
    
    

        
if __name__ == '__main__':
    build_tree()
