# Implementation of Trees in Python

# root is an instance of TreeNode
# parent is an "instance" of root consequently an "instance" of TreeNode
# child is an "instance" of parent which is an "instance" of root consequently an instance of TreeNode



class TreeNode(): # Recursive data structure inwhich each Node could be a tree itself
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
        
    # Add children or sub-nodes to the tree
    def add_child(self, child): # child node is of type TreeNode and is being added to a parent node which itself is an instance of the TreeNode Class
        child.parent = self # child is an instance of the TreeNode class and has a property/attribute parent and I am setting it to the current instance 
        self.children.append(child)
    
    def get_tree_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
        
    def print_tree(self): # Print the tree structure of the TreeNode class
        add_spaces = " " * (self.get_tree_level() + 3) # create an empty string add_spaces of length level + 3
        # result = [on_true] if [expression] else [on_false] 
        add_spaces = add_spaces + "|--" if self.parent else "" 
        print(add_spaces + self.data) # Prints the Root Node
        if self.children: # Check if parent node exists then
            for child in self.children: # for each parent node, 
                child.print_tree() # print the children of the parent node
        
        
        
        
        
def build_tree():
    root = TreeNode("Electronics") #Creating a root node with data = "Electronic"
    
    laptop = TreeNode("Laptop") # Creating a parent Node with data = "Laptop"
    
    # Add children or leaf nodes to the parent Laptop
    laptop.add_child(TreeNode("Apple"))
    laptop.add_child(TreeNode("Toshiba"))
    laptop.add_child(TreeNode("HP"))
    
    
    cell_phone = TreeNode("Cell Phone") # Creating a parent Node with data = "Cell Phone"
    
    # Add children or leaf nodes to the parent Cell Phone
    cell_phone.add_child(TreeNode("iPhone"))
    cell_phone.add_child(TreeNode("Samsung"))
    cell_phone.add_child(TreeNode("Huawei"))

    
    tv = TreeNode("TV") # Creating a parent Node with data = "TV"
    
    # Add children or leaf nodes to the parent TV
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Phillips"))
    
    
    root.add_child(laptop) # Adding a parent node, "Laptop" to the root Node
    root.add_child(cell_phone) # Adding a parent node, "Cell Phone" to the root Node
    root.add_child(tv) # Adding a parent node, "TV" to the root Node
    
    root.print_tree()
    #print(tv.get_tree_level()) # This should return 1
    

        
if __name__ == '__main__':
    build_tree()    
