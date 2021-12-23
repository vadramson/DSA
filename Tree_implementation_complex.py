# Implementation of Trees in Python (Multi-Parents attributes)

# root is an instance of TreeNode
# parent is an "instance" of root consequently an "instance" of TreeNode
# child is an "instance" of parent which is an "instance" of root consequently an instance of TreeNode


class TreeNode():
    def __init__(self, data, desig):
        self.data = data
        self.desig = desig
        self.children = []
        self.parent = None
        
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    
    def get_tree_level(self):
        pa = self.parent
        lev = 0
        
        while pa:
            lev += 1
            pa = pa.parent
        return lev
        
        
    def print_tree(self, attr: int):
        # making Spaces and lines to show hirachy
        add_space = " "  * (self.get_tree_level() * 2)
        add_space = add_space + "|--" if self.parent else ""
        data_option = ""
        if attr == 0:
            data_option = str(self.data) + " (" + str(self.desig) + ")"
        elif attr == 1:
            data_option = str(self.data)
        elif attr == 2:
            data_option = str(self.desig) 
        else:
            return print("Enter\n 0 to print both Name and Desigation, \n 1 to print ONLY name, \n 2 to print ONLY Designation")
        
        print(add_space , data_option)
        
        for child in self.children:
            child.print_tree(attr)

# Creating an organizational Chart        
def build_tree():
    root = TreeNode("Vadrama NDISANG", "CEO")
    
    # Adding members of the IT department
    cto = TreeNode("Vadson Bob", "CTO")
    cto.add_child(TreeNode("Bobby Vad", "Dev"))
    cto.add_child(TreeNode("vadrams Vadramson", "Data"))
    cto.add_child(TreeNode("Ndisang Vadson", "DBA"))
    
    
    # Adding members of the Communications department
    cio = TreeNode("Alphonso lambertini", "CIO")
    cio.add_child(TreeNode("Pascal Fab", "FB"))
    cio.add_child(TreeNode("Anderson Markus", "Tw"))
    cio.add_child(TreeNode("Eliot Bolt", "YB"))
    
    # Adding members of the Productions department
    cpo = TreeNode("Martin Hublot", "CPO")
    cpo.add_child(TreeNode("Emilia Augustasis", "RM"))
    cpo.add_child(TreeNode("Henry Jule", "T1"))
    cpo.add_child(TreeNode("Chick Ebot", "TF"))
    
    
    # Adding Parents to the Tree
    root.add_child(cto)
    root.add_child(cio)
    root.add_child(cpo)
    
    # Printing the Built Tree
    root.print_tree(0) # Both Name and Designation
    #root.print_tree(1) # Just Name
    #root.print_tree(2) # Just Designation
    #root.print_tree(3) # Cat Error
    

if __name__ == '__main__':
    build_tree()
