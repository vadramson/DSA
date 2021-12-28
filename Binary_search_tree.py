"""
			  17
			/    \
		   /      \
		  /	       \		  
		 4          20
		 /\			/\	
	    /  \       /  \
	   /    \     /    \
	  1      9    18    23
						  \
						   \
							\ 
						     34
							 
"""							 

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
    
    # Visit Left subtree, then Root node and finaly Right subtree
    def in_order_traversal(self):  # Left - Root - Right
        elements = []
        
        # Getting all elements of the Left Subtree    
        if self.left:
            elements += self.left.in_order_traversal() # Recursively get all the elements of the left subtree and add them into the list
        elements.append(self.data) # Adding the root node to the list
        
        # Getting all elements of the Right Subtree    
        if self.right:
            elements += self.right.in_order_traversal() # Recursively get all the elements of the right subtree and add them into the list
        return elements
        
    # Get all elements from the Root node then the left subtree and finanally the Right subtree 
    def pre_order_traversal(self): # Root - Left - Right
        elements = []
        
        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()  # Recursively get all the elements of the left subtree and add them into the list
        
        if self.right:
            elements += self.right.pre_order_traversal()  # Recursively get all the elements of the right subtree and add them into the list

        
        return elements # get the Root node element
        
    # Get all elements from the Right subtree then the left subtree and finally the Root node    
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()  # Recursively get all the elements of the left subtree and add them into the list
        
        if self.right:
            elements += self.right.post_order_traversal()  # Recursively get all the elements of the right subtree and add them into the list
            
        elements.append(self.data) # Get the Root node element
        
        return elements
        
        
    def search_element(self, elem): # complexity of log n O(log n)
        if self.data == elem:
            return True
        elif elem < self.data:
            # This means if present, element would be on the left 
            if self.left:
               return self.left.search_element(elem)  
            else:
                return False
            
        else:
            # This means if present, element would be on the right
            if self.right:
                return self.right.search_element(elem)  
            else:
                return False
    
    
    def sum_of_all_elements_in_tree(self):
        return sum(self.in_order_traversal())
        
    def max_element_in_tree(self):
        return max(self.in_order_traversal())    
    
    def min_element_in_tree(self):
        return min(self.in_order_traversal())    
    
    
# Tree Builder helper method
def build_binary_tree(lst_elem: list):
    if len(lst_elem) >1:
        root_node = BinaryTreeNode(lst_elem[0])
        for i in lst_elem[1:]:
            root_node.add_child(i)
       
        #root_node.search_element(20)
        #print(root_node.in_order_traversal())
        return root_node
    else:
        return print("Insufficient number of elements")
        

if __name__ == '__main__':
   mt = build_binary_tree([17, -5, 4, 1, 20, 9, -1, 23, 18, 0, 34])
   print("In Order Traversal", mt.in_order_traversal())
   print("Post Order Traversal", mt.post_order_traversal())
   print("Pre Order Traversal", mt.pre_order_traversal())
   print(mt.search_element(20))
   print("Sum of all elemnts in tree", mt.sum_of_all_elements_in_tree())
   print("Max element in tree is", mt.max_element_in_tree())
   print("Min element in tree is", mt.min_element_in_tree())
            
            
            
